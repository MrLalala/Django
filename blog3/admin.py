# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Article, Person


# admin.site.register(Article)
# Register your models here.
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', )
    search_fields = ('pub_date', )
    list_filter = ('update_time', )

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        obj.save()


class PersonAdmin(admin.ModelAdmin):
    list_display = ('full_name', )


admin.site.register(Article, ArticleAdmin)
admin.site.register(Person, PersonAdmin)
