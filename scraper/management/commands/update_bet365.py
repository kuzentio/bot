import logging
import re
from urllib.parse import quote

import requests
from django.core.management import BaseCommand

from scraper.models import Race

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
        token = re.sub('/', '#', race.bet365_data['token'])

        url = race.bet365_data['url'].format(
            token=quote(token),
        )
        response = requests.get(url)
        horses = [horse for horse in response.text.split('|') if 'OD' in horse]
        # TODO: not closed issue because of technical maintain issue in bet365
