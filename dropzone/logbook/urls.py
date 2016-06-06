from django.conf.urls import url
from . import views

app_name = 'logbook'

urlpatterns = [
    url(r'^$', views.index),
]
