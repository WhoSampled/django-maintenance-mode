# -*- coding: utf-8 -*-

from django.contrib.sessions.models import Session

from maintenance_mode import io, settings


def get_maintenance_mode():

    value = io.read_file(settings.MAINTENANCE_MODE_STATE_FILE_PATH, '0')

    if not value in ['0', '1']:
        raise ValueError('state file content value is not 0|1')

    value = bool(int(value))
    return value


def set_maintenance_mode(value):

    if not isinstance(value, bool):
        raise TypeError('value argument type is not boolean')

    if settings.MAINTENANCE_MODE_EXPIRE_DB_SESSIONS:
        Session.objects.all().delete()

    value = str(int(value))
    io.write_file(settings.MAINTENANCE_MODE_STATE_FILE_PATH, value)
