#coding=utf8
from django.db import models

class State(models.Model):
	"""
	Clase informacion de estados geograficos
	"""
	name = models.CharField(max_length=32)

	def __unicode__(self):
		return self.name


