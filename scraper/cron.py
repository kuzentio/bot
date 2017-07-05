from django_cron import CronJobBase, Schedule
from django.core.management import call_command

from scraper.models import Race


class MyCronJob(CronJobBase):
    RUN_EVERY_MINS = 5

    schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
    code = 'my_app.my_cron_job'    # a unique code

    def do(self):
        for race in Race.objects.all():
            call_command('update_providers', race_id=race.id)
