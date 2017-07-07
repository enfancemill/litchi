# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import JsonResponse


class JsonResponseRedirect(JsonResponse):
    status = 302

    def __init__(self, location, **kwargs):
        self.location = location
        data = {
            'status': self.status,
            'location': self.location,
        }
        super(JsonResponseRedirect, self).__init__(data=data, **kwargs)
