from django.shortcuts import render, get_object_or_404

from scraper.models import Horse, Race


def index(request):
    race_id = request.GET.get('race_id', 1)
    race = get_object_or_404(
        Race, id=race_id,
    )

    horses = Horse.objects.filter(
        races=race,
        paddypowerbet__race=race,
        williamhillbet__race=race,
        skybet__race=race,
    ).values(
        'name',
        'id',

        'paddypowerbet__odd', 'paddypowerbet__probability',
        'williamhillbet__odd', 'williamhillbet__probability',
        'skybet__odd', 'skybet__probability',
        'bet365bet__odd', 'bet365bet__probability',
    )

    context = {
        'horses': horses,
        'race': race,
    }

    return render(request, 'index.html', context)
