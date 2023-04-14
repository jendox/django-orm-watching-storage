import datetime
from django.utils.timezone import localtime
from datacenter.models import Visit


def get_duration(visit: Visit) -> datetime.timedelta:
    if not visit.leaved_at:
        visit.leaved_at = localtime()
    return visit.leaved_at - visit.entered_at


def format_duration(duration: datetime.timedelta) -> str:
    total_seconds = duration.total_seconds()
    hours = int(total_seconds // 3600)
    minutes = int((total_seconds - hours*3600) // 60)
    seconds = int(total_seconds - hours*3600 - minutes*60)
    return f"{hours}:{minutes}:{seconds}"


def is_visit_long(visit: Visit, minutes: int = 60):
    return True if get_duration(visit).total_seconds() >= minutes*60 else False
