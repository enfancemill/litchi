from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.SessionView.as_view(), name='session'),
]
