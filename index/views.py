from django.shortcuts import render, get_object_or_404

from scraper.models import Horse, Race


def index(request, race_id):
    race = get_object_or_404(
        Race, id=race_id
    )
    horses = Horse.objects.filter(
        races=race
    ).values(
        'name', 'paddypowerbet__odd', 'paddypowerbet__probability',
        'name', 'williamhillbet__odd', 'williamhillbet__probability',
        'name', 'bet365bet__odd', 'bet365bet__probability',
    )
    context = {
        'horses': horses,
        'race': race,
    }

    return render(request, 'index.html', context)
