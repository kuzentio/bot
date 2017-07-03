from django.contrib import admin
from django_extensions.db.fields.json import JSONField

from prettyjson import PrettyJSONWidget
from scraper.models import Race, Horse, PaddyPowerBet, WilliamHillBet, Bet365Bet


class ProviderAdmin(admin.ModelAdmin):
    list_display = ('horse', 'race', 'odd', 'probability', 'created', 'modified',)
    ordering = ('id', )


class RaceAdmin(admin.ModelAdmin):
    formfield_overrides = {
        JSONField: {'widget': PrettyJSONWidget}
    }


admin.site.register(Race, RaceAdmin)
admin.site.register(Horse)
admin.site.register(PaddyPowerBet, ProviderAdmin)
admin.site.register(WilliamHillBet, ProviderAdmin)
admin.site.register(Bet365Bet, ProviderAdmin)

