# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import json

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views import View
from captcha.helpers import captcha_image_url
from captcha.models import CaptchaStore

from logic.ext_django.response import JsonResponseRedirect
from logic.utils.decorators import nonlogin_required
from .forms import SessionLoginForm


class SessionView(View):

    #@method_decorator(nonlogin_required)
    def get(self, request):
        captcha_key = CaptchaStore.generate_key()
        captcha_url = captcha_image_url(captcha_key)
        context = {
            'captcha_key': captcha_key,
            'captcha_url': captcha_url,
        }
        return render(request, 'login.html', context)

    #@method_decorator(nonlogin_required)
    def put(self, request):
        data = json.loads(request.body)
        form = SessionLoginForm(data)
        captcha_key = CaptchaStore.generate_key()
        captcha_url = captcha_image_url(captcha_key)
        if form.is_valid():
            data = form.cleaned_data
            username = data.get('username')
            password = data.get('password')
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return JsonResponseRedirect('/')
            else:
                error_msg = '用户名或密码错误'
                context = {
                    'error_msg': error_msg,
                    'captcha_key': captcha_key,
                    'captcha_url': captcha_url,
                }
                return render(request, 'login.html', context)
        else:
            context = {
                'form': form,
                'captcha_key': captcha_key,
                'captcha_url': captcha_url,
            }
            return render(request, 'login.html', context)

    @method_decorator(login_required(redirect_field_name=None, login_url='/session/'))
    def delete(self, request):
        logout(request)
        return JsonResponseRedirect('/')
