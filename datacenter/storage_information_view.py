from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render
from datacenter.models import get_duration, format_duration


def storage_information_view(request):
    # Программируем здесь
    non_closed_visits = []
    visits = Visit.objects.filter(leaved_at=None)
    for visit in visits:
        visit_time = get_duration(visit)
        duration = format_duration(visit_time)
        visitor = visit.passcard.owner_name

        who_in_storage = {
            "who_entered": visitor,
            "entered_at": visit.entered_at,
            "duration": duration,
        }
        non_closed_visits.append(who_in_storage)

    context = {
        "non_closed_visits": non_closed_visits,  # не закрытые посещения
    }
    return render(request, 'storage_information.html', context)
