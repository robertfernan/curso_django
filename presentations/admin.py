#coding=utf8
from django.contrib import admin
from .models import Presentation, Track


admin.site.register(Presentation)
admin.site.register(Track)
