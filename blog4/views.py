# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render


def index(request):
    return render(request, 'blog4/index.html')


def columns(request):
    return render(request, 'blog4/columns.html')
# Create your views here.
