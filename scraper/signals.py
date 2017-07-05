import json

from channels import Group
from django.db.models.signals import post_save
from django.dispatch import receiver

from scraper.models import PaddyPowerBet, WilliamHillBet, Bet365Bet, SkyBet


@receiver(post_save, sender=PaddyPowerBet)
@receiver(post_save, sender=WilliamHillBet)
@receiver(post_save, sender=Bet365Bet)
@receiver(post_save, sender=SkyBet)
def providers_post_save(sender, **kwargs):
    instance = kwargs.get('instance')
    prefix = ''
    if isinstance(instance, PaddyPowerBet):
        prefix = 'pp'
    if isinstance(instance, WilliamHillBet):
        prefix = 'wh'
    if isinstance(instance, Bet365Bet):
        prefix = 'b3'
    if isinstance(instance, SkyBet):
        prefix = 'sb'
    text = {
        'uniid': '{0}_{1}_{2}'.format(prefix, instance.horse.id, instance.race.id),
        'odd': instance.odd,
        'probability': instance.probability,
    }
    Group('odds').send({'text': json.dumps(text)})

