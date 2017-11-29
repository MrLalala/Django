"""New URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from learn import views as ler_views
from cal import views as cal_views
from form import views as form_views
from form2 import views as form2_views
from blog4 import views as blog4_views

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    # url(r'^add$', cal_views.add, name='add'),
    # url(r'^new_add2/(\d+)/(\d+)/$', cal_views.add2, name='add2'),
    # url(r'^cal$', cal_views.index, name='home'),
    # url(r'^add2/(\d+)/(\d+)/$', cal_views.old_redirect),
    # url(r'^$', ler_views.home, name='home_learn'),
    # url(r'^hello$', ler_views.index, name='hello'),
    # url(r'^add/$', form_views.add, name='add'),
    # url(r'^home/$', form_views.home, name='home')
    # url(r'^$', form2_views.index, name='home'),
    url(r'^home/$', blog4_views.index, name='b4index'),
    url(r'^column/$', blog4_views.columns, name='b4column'),
]

