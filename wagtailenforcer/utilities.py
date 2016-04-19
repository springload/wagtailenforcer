# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import pyclamd

from django.utils.translation import ugettext_lazy as _
from django.conf import settings
from django.contrib import messages
from .exceptions import EnforcerVirusException


def check_for_virus(instance):
    has_virus, name = is_infected(instance.file.read())

    if has_virus:
        raise EnforcerVirusException(_('Virus "{}" was detected').format(name))

    return instance


def is_infected(stream):
    clam = get_clam()
    if getattr(settings, 'CLAMAV_ACTIVE', False) is False or clam is None:
        return None, ''

    result = clam.scan_stream(stream)
    if result:
        return True, result['stream'][1]

    return False, ''


def get_clam():
    try:
        clam = pyclamd.ClamdUnixSocket()

        # test if server is reachable
        clam.ping()

        return clam
    except pyclamd.ConnectionError:
        # if failed, test for network socket
        cd = pyclamd.ClamdNetworkSocket()
        try:
            cd.ping()
            return clam
        except pyclamd.ConnectionError:
            raise ValueError('could not connect to clamd server either by unix or network socket')
