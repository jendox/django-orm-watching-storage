import datetime

from django.utils.timezone import localtime

from datacenter.models import Visit
from django.shortcuts import render


def get_duration(visit: Visit) -> datetime.timedelta:
    if not visit.leaved_at:
        visit.leaved_at = localtime()
    return visit.leaved_at - visit.entered_at


def format_duration(duration) -> str:
    total_seconds = duration.total_seconds()
    hours = int(total_seconds // 3600)
    minutes = int((total_seconds - hours*3600) // 60)
    seconds = int(total_seconds - hours*3600 - minutes*60)
    return f"{hours}:{minutes}:{seconds}"


def is_visit_long(visit, minutes=60):
    return True if get_duration(visit).total_seconds() >= minutes*60 else False


def storage_information_view(request):
    # Программируем здесь

    non_closed_visits = [
        {
            'who_entered': visit.passcard.owner_name,
            'entered_at': visit.entered_at,
            'duration': format_duration(get_duration(visit)),
        }
        for visit in Visit.objects.filter(leaved_at=None)
    ]
    context = {
        'non_closed_visits': non_closed_visits,  # не закрытые посещения
    }
    return render(request, 'storage_information.html', context)
