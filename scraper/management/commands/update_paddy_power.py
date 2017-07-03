import json
import logging
import re

from django.core.management import BaseCommand
import requests

from scraper.models import PaddyPowerBet, Race, Horse

log = logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s [%(levelname)s] %(message)s',
    datefmt='%m/%d/%Y %I:%M:%S %p'
)
logger = logging.getLogger(log)


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
        url = race.paddy_power_data['url'].format(
            event_id=race.paddy_power_data.get('event_id')
        )
        response = requests.get(url)
        parameters = re.findall(r'\(\s*({[^)]+?})\s*\)', response.text)[0]
        race_regexp = r'(\[.*?\])'
        races_data = re.findall(race_regexp, parameters)
        horses = json.loads(races_data[0])
        for horse_in_race in horses:
            horse_name = horse_in_race['horse_names'].get('en')
            if horse_name is None:
                continue
            horse, _ = Horse.objects.get_or_create(name=horse_name)
            _, _ = PaddyPowerBet.objects.update_or_create(
                race=race,
                horse=horse,
                defaults={
                    'odd': horse_in_race.get('lp_num'),
                    'probability': horse_in_race.get('has_rp'),
                }
            )
        logger.info("Done.")
