from django.conf.urls import url, include
from django.contrib import admin

from logbook.views import index

urlpatterns = [
    url(r'^$', index),
    url(r'^admin/', admin.site.urls),
    url(r'^logbook/', include('logbook.urls')),
]
