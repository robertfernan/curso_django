#coding=utf8
from django.contrib import admin
from .models import Sponsor, SponsorshipType


admin.site.register(Sponsor)
admin.site.register(SponsorshipType)
