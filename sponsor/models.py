#coding=utf8
from django.db import models


class SponsorshipType(models.Model):
	"""
	Clase informacion de referente a los SponsorShip Type
	"""
	name = models.CharField(max_length=64)
	description = models.TextField()
	rango_start = models.IntegerField(null=True, blank=True)
	rango_end = models.IntegerField(null=True, blank=True)

	def __unicode__(self):
		return self.name


class Sponsor(models.Model):
	"""
	Clase informacion de referente a los Sponsor
	"""
	sponsorship_type = models.ForeignKey(SponsorshipType)
	name = models.CharField(max_length=64)
	description = models.TextField()
	logo = models.ImageField(upload_to='sponsor_logos/')
	website = models.URLField(max_length=250)

	def __unicode__(self):
		return self.name


