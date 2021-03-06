from django.db import models
from django_extensions.db.fields.json import JSONField
from django_extensions.db.models import TimeStampedModel


class Horse(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Race(models.Model):
    name = models.CharField(max_length=255)
    horses = models.ManyToManyField(Horse, related_name='races', blank=True)

    paddy_power_data = JSONField(blank=True, help_text='"url" and "event_id" is required')
    bet365_data = JSONField(blank=True)
    william_hill_data = JSONField(blank=True, help_text='"url" and "template_name" is required')
    sky_bet_data = JSONField(blank=True, help_text='"url" and "event_id" is required')

    def __str__(self):
        return self.name


class OddsMixin(models.Model):
    odd = models.IntegerField(blank=True, null=True)
    probability = models.IntegerField(blank=True, null=True)

    def deactivate_odds(self):
        self.odd = None
        self.probability = None

    class Meta:
        abstract = True


class PaddyPowerBet(TimeStampedModel, OddsMixin):
    horse = models.ForeignKey(Horse)
    race = models.ForeignKey(Race)

    def __str__(self):
        return '{name} {odd}/{probability}'.format(
            name=self.horse.name,
            odd=self.odd,
            probability=self.probability,
        )


class WilliamHillBet(TimeStampedModel, OddsMixin):
    horse = models.ForeignKey(Horse)
    race = models.ForeignKey(Race)

    def __str__(self):
        return '{name} {odd}/{probability}'.format(
            name=self.horse.name,
            odd=self.odd,
            probability=self.probability,
        )


class Bet365Bet(TimeStampedModel, OddsMixin):
    horse = models.ForeignKey(Horse)
    race = models.ForeignKey(Race)

    def __str__(self):
        return '{name} {odd}/{probability}'.format(
            name=self.horse.name,
            odd=self.odd,
            probability=self.probability,
        )


class SkyBet(TimeStampedModel, OddsMixin):
    horse = models.ForeignKey(Horse)
    race = models.ForeignKey(Race)

    def __str__(self):
        return '{name} {odd}/{probability}'.format(
            name=self.horse.name,
            odd=self.odd,
            probability=self.probability,
        )
