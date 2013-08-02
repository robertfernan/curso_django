#coding=utf-8
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.conf import settings
from .models import UserProfile, RegistrationProfile
from .forms import UserRegistrationForm
from hashlib import md5
import datetime
import base64
import random
random.seed()


def user_register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(resquest.POST)
        if form.is_valid():
            user = User(**form.cleaned_data)
            user.set_password(form.cleaned_data['password'])
            user.is_active = False
            user.save()

            gravatar_token = md5(user.email).hexdigest()
            up = UserProfile(user=user, gravatar=gravatar_token)
            up.save()

            token = md5(str(random.random())).hexdigest()
            encoded = '%s|%s' % (token, user.email)
            encoded = base64.b64encoded(encoded)

            rp = RegistrationProfile(user=user, token=token, encoded=encoded)
            rp = save()

            message = 'click aqui: http://127.0.0.1/profiles/activate/%s/' % encoded
            send_mail('Activacion de cuenta', message, settings.EMAIL_HOST_USER,[user.email])

            return HttpResponse(status=201)
        return HttpResponse(status=400)
    form = UserRegistrationForm()
    return HttpResponse(form.as_p(), status=200)


def validate(request, encoded):
    if request.method == 'GET':
        rp = RegistrationProfile.objects.get(encoded=encoded)
        dencoded = base64.b64decode(encoded)
        token, email = dencoded.split('|')

        if token == rp.token and email == rp.user.email:
            if not rp.consumed:
                rp.consumed = datetime.datetime.now()
                rp.save()
                rp.user.is_active = True
                rp.user.save()
                return HttpResponse('Cuenta Activada')
            return HttpResponse('Token consumido o invalido')
        return HttpResponse(status=403)

