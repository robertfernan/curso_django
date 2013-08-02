#coding=utf-8
from django.test import TestCase
from django.test.client import Client
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from .factories import UserProfileFactory, RegistrationProfileFactory
from .models import RegistrationProfile



class UserRegistrationTest(TestCase):
    def setUp(self):
        pass

    def test_user_registration_ok(self):
        pass


class UserValidationTest(TestCase):
    def setUp(self):
        self.reg_profile = RegistrationProfileFactory()
        self.reg_profile.user.is_active = False
        self.reg_profile.user.save()
        self.reg_profile.save()
        self.user_profile =  UserProfileFactory(user=self.reg_profile.user)
        self.user_profile.save()
        self.client = Client()


    def test_user_validation_ok(self):
        self.assertFalse(self.reg_profile.consumed)

        url_args = {
            'encoded': self.reg_profile.encoded,
        }
    
        response = self.client.get(reverse('user-validate', kwargs=url_args))

        user = User.objects.get(id=self.reg_profile.user.id)
        rp = RegistrationProfile.objects.get(id=self.reg_profile.id)
        self.assertTrue(user.is_active)
        self.assertTrue(rp.consumed)