# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse


# 只有一个request，则参数通过get或者post传递
def add(request):
    # GET.get(key, default)
    a = request.GET.get('a', 0)
    b = request.GET.get('b', 0)
    c = int(a) + int(b)
    return HttpResponse(str(c))


# 有其他参数就要注意在地址添加相应的参数
def add2(request, a, b):
    c = int(a) + int(b)
    return HttpResponse(str(c))
# Create your views here.
