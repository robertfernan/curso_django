#coding=utf8
from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    """
    Clase para almacenar informacion referente a 
    Perfiles de usuario
    """
    user = models.OneToOneField(User)
    gravatar = models.CharField(max_length=32)
    about = models.TextField(null=True, blank=True)
    twitter = models.CharField(max_length=16, null=True, blank=True)
    blog = models.URLField(max_length=200, null=True, blank=True)

    def __unicode__(self):
        return self.twitter



class RegistrationProfile(models.Model):
    """
    clase para almacenar daos de validacion
    de los usuarios cuando se registran
    """
    user = models.OneToOneField(User)
    token = models.CharField(max_length=32)
    encoded = models.CharField(max_length=256)
    created = models.DateTimeField(auto_now_add=True)
    consumed = models.DateTimeField(null=True, blank=True)
    