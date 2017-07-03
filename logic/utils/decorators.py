# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from functools import wraps

from django.http import HttpResponseRedirect


def optional_parameter(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if len(args) == 1 and len(kwargs) == 0 and callable(args[0]):
            return func(args[0])
        else:
            return lambda realfunc: func(realfunc, *args, **kwargs)
    return wrapper


@optional_parameter
def nonlogin_required(func, redirect_url='/'):
    @wraps(func)
    def wrapper(request, *args, **kwargs):
        if request.user.is_authenticated():
            return HttpResponseRedirect(redirect_url)
        return func(request, *args, **kwargs)
    return wrapper
