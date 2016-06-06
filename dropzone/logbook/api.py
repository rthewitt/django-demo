from .models import *
from rest_framework import serializers, viewsets

class ParachuteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Parachute
        fields = ('name', 'size')

class ParachuteViewSet(viewsets.ModelViewSet):
    queryset = Parachute.objects.all()
    serializer_class = ParachuteSerializer
