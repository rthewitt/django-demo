from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth.views import login, logout

from logbook.views import index

urlpatterns = [
    url(r'^$', index),
    url(r'^admin/', admin.site.urls),
    url(r'^logbook/', include('logbook.urls')),
    url(r'^accounts/login/$', login, name='login'),
    url(r'^accounts/logout/$', logout, name='logout', kwargs={'next_page': '/'})
]
