from django.contrib import admin
from .models import Aircraft, Parachute, Container, Rig

# Register your models here.
admin.site.register(Aircraft)
admin.site.register(Parachute)
admin.site.register(Container)
admin.site.register(Rig)
