import json
import logging
import re

from bs4 import BeautifulSoup
from django.core.management import BaseCommand
import requests

from scraper.models import PaddyPowerBet, Race, Horse, SkyBet

log = logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s [%(levelname)s] %(message)s',
    datefmt='%m/%d/%Y %I:%M:%S %p'
)
logger = logging.getLogger(log)


def execute_horse_name(tr):
    horse_name_txt = tr.find('div', {'class': 'oc-horse'}).find('h4').text
    horse_name_list = re.sub(' +', ' ', horse_name_txt).split(' ')
    horse_name_clean_list = horse_name_list[1:len(horse_name_list) - 1]
    horse_name = ' '.join(horse_name_clean_list)

    return horse_name


def execute_horse_odd(tr):
    odd_element = tr.find('td', {'class': 'win'})
    odd = int(odd_element.attrs['data-oc-num'])
    probability = int(odd_element.attrs['data-oc-den'])

    return odd, probability


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

        url = 'https://www.skybet.com/horse-racing/newmarket/event/20915135'
        response = requests.get(url)
        horse_in_race__ids = []
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            trs = soup.findAll('tr', {"id": lambda x: x and x.startswith('horseDetailControl')})
            if not trs:
                logger.info("Remote service is unavailable.")
            for tr in trs:
                horse_name = execute_horse_name(tr)
                odd, probability = execute_horse_odd(tr)
                horse, _ = Horse.objects.get_or_create(name=horse_name)

                if not race.horses.filter(id=horse.id).exists():
                    race.horses.add(horse)

                _, _ = SkyBet.objects.update_or_create(
                    race=race,
                    horse=horse,
                    defaults={
                        'odd': odd,
                        'probability': probability,
                    }
                )
                horse_in_race__ids.append(horse.id)
        for horse in SkyBet.objects.filter(race=race).exclude(horse__id__in=horse_in_race__ids):
            horse.deactivate_odds()
            horse.save()

        logger.info("Done.")
