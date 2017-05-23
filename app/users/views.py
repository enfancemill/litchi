# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.backends import ModelBackend

from .models import Member


class EmailModelBackend(ModelBackend):

    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user = Member.objects.get(email=username)
        except Member.DoesNotExist:
            return None
        else:
            if user.check_password(password) and self.user_can_authenticate(user):
                return user
