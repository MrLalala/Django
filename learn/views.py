# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse(u"欢迎光临")


def home(request):
    return render(request, 'home.html')
# Create your views here.
