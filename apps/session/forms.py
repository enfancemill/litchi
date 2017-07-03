# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django import forms
from captcha.fields import CaptchaField


class SessionLoginForm(forms.Form):
    username = forms.EmailField(
        required=True,
        error_messages={
            'invalid': '邮箱格式错误',
            'required': '用户名不能为空',
        },
    )
    password = forms.CharField(
        required=True,
        error_messages={
            'required': '密码不能为空',
        },
    )
    captcha = CaptchaField(
        required=True,
        error_messages = {
            'invalid': '验证码错误',
            'required': '验证码不能为空',
        },
    )
