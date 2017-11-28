# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse


def add(request):
    a = int(request.GET.get('a', None))
    b = int(request.GET.get('b', None))
    return HttpResponse(a + b)


def home(request):
    return render(request, 'add.html')
# Create your views here.
