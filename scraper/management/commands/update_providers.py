import logging
from django.core.management import BaseCommand
from django.core.management import call_command

log = logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s [%(levelname)s] %(message)s',
    datefmt='%m/%d/%Y %I:%M:%S %p'
)
logger = logging.getLogger(log)


class Command(BaseCommand):
    COMMANDS = [
        'update_paddy_power',
        'update_william_hill',
        'update_sky_bet',
    ]

    def add_arguments(self, parser):
        parser.add_argument(
            '--race_id',
            dest="race_id",
            type=int,
            help='Enter Horse race ID',
        )

    def handle(self, *args, **options):
        race_id = options.get('race_id')

        if not race_id:
            logger.info("Please provide race id.")
            return

        for command in self.COMMANDS:
            call_command(command, race_id=race_id)
