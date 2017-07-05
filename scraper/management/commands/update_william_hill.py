import logging
from bs4 import BeautifulSoup

from django.core.management import BaseCommand
import requests

from scraper.models import Horse, WilliamHillBet, Race

log = logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s [%(levelname)s] %(message)s',
    datefmt='%m/%d/%Y %I:%M:%S %p'
)
logger = logging.getLogger(log)

URL = 'http://sports.williamhill.com/bet/en-gb/betting/e/11127481/ap/{event_id}'


def get_horse_name_from_row(row):
    text = row.find('td').text
    result = [el for el in text.split() if el not in ['View', 'Tips']]
    horse_name = ' '.join(result).encode('utf-8')
    return horse_name


def get_horse_odd_from_row(row):
    text = row.find_all('a')[1].text
    odds, probability = text.split()[0].split('/')

    return odds, probability


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument(
            '--race_id',
            dest="race_id",
            type=int,
            help='Enter Horse race ID',
        )

    def handle(self, *args, **options):
        race_id = options.get('race_id')
        try:
            race = Race.objects.get(id=race_id)
        except Race.DoesNotExist:
            logger.info("provide existing race id")
            return
        template_name = race.william_hill_data['template_name']
        event_id = race.william_hill_data['event_id']
        url = race.william_hill_data['url']

        response = requests.get(url.format(
            template_name=template_name,
            event_id=event_id,
        ))
        horse_in_race__ids = []
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            rows = soup.find("table").find("tbody").find_all("tr")
            for num, row in enumerate(rows):
                if num == 0:
                    continue

                horse_name = get_horse_name_from_row(row)
                odd, probability = get_horse_odd_from_row(row)

                horse, _ = Horse.objects.get_or_create(name=horse_name)
                _, _ = WilliamHillBet.objects.update_or_create(
                    race=race,
                    horse=horse,
                    defaults={
                        'odd': odd,
                        'probability': probability,
                    }
                )
                horse_in_race__ids.append(horse.id)
        for horse in WilliamHillBet.objects.filter(race=race).exclude(horse__id__in=horse_in_race__ids):
            horse.deactivate_adds()
            horse.save()

        logger.info("Done.")
