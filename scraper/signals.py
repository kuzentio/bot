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
    text = {
        'uniid': instance.uniid,
        'odd': instance.odd,
        'probability': instance.probability,
    }
    Group('odds').send({'text': json.dumps(text)})

