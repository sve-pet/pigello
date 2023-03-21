from django.contrib.auth.models import User, Group
from django.http import Http404
from rest_framework import serializers, status
from rest_framework.response import Response

from planetary_play.models import Planet, Moon


class PlanetSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Planet
        fields = ['name', 'mass', 'vol', 'gravity', 'planet_id']


class MoonSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Moon
        fields = ['name', 'mass', 'vol', 'gravity', 'planet', 'moon_id']

    def destroy(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            self.perform_destroy(instance)
        except Http404:
            pass
        return Response(status=status.HTTP_204_NO_CONTENT)