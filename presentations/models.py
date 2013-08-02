#coding=utf8
from django.db import models
from django.contrib.auth.models import User


class Track(models.Model):
	"""
	Clase informacion de referente a Tracks de la conferencia
	"""
	name = models.CharField(max_length=32)
	room = models.CharField(max_length=256)
	description = models.TextField()

	def __unicode__(self):
		return '%s  |  %s' % (self.name, self.room)


class Presentation(models.Model):
	"""
	Clase informacion de Presentaciones
	"""
	speakers = models.ManyToManyField(User)
	track = models.ForeignKey(Track)
	title = models.CharField(max_length=256)
	description = models.TextField()
	requirements = models.TextField()
	approved = models.BooleanField(default=False)
	start = models.DateTimeField(auto_now_add=True)
	duration = models.IntegerField()
	slides = models.URLField(max_length=256, blank=True, null=True)

	def __unicode__(self):
		return self.title


