# coding:utf-8
from django.conf import settings as origin_settings


def settings(request):
    return {'settings': origin_settings}


def ip_address(request):
    return {'ip_address': request.META['REMOTE_ADDR']}