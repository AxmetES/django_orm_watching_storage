from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
from datacenter.models import get_duration, format_duration, is_visit_long


def passcard_info_view(request, passcode):
    this_passcard_visits = []
    try:
        passcard = Passcard.objects.get(passcode=passcode)
        visits = Visit.objects.filter(leaved_at__isnull=False, passcard__owner_name__contains=passcard)
    except ObjectDoesNotExist:
        print("Either the entry or blog doesn't exist.")

    for visit in visits:
        entered_at = visit.entered_at
        visit_time = get_duration(visit)
        duration = format_duration(visit_time)
        is_strange = is_visit_long(visit)

        passcard_visit = {
            "entered_at": entered_at,
            "duration": duration,
            "is_strange": is_strange,
        }
        this_passcard_visits.append(passcard_visit)

    # Программируем здесь

    context = {
        "passcard": passcard,
        "this_passcard_visits": this_passcard_visits
    }
    return render(request, 'passcard_info.html', context)
