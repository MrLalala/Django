# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse(u"欢迎光临")


def home(request):
    string = u'Study for Django!'
    list1 = [1, 2, 3, 4, 5]
    list2 = range(100)
    dict1 = {'site': u'my site', 'content': u'Django'}
    return render(request, 'learn/home.html',
                  {'string': string,
                   'list': list1,
                   'dict': dict1,
                   'list2': list2,
                   'request': request,
                   'test': 100})
# Create your views here.
