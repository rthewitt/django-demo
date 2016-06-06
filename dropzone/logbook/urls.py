from .api import ParachuteViewSet
from rest_framework import routers
from django.conf.urls import url, include
from . import views

app_name = 'logbook'

router = routers.DefaultRouter()
router.register(r'parachutes', ParachuteViewSet)

urlpatterns = [
    url(r'^$', views.index),
    url(r'^jumps$', views.jumps, name='jumps'),
    url(r'^api/', include(router.urls)),
]
