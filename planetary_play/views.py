from django.http import JsonResponse
from django.shortcuts import render
from django.contrib.auth.models import User, Group
from rest_framework import viewsets, status, serializers
from rest_framework.decorators import api_view
from rest_framework.response import Response

from planetary_play.external_api import get_planets
from planetary_play.models import Planet, Moon
from planetary_play.serializers import PlanetSerializer, MoonSerializer


class PlanetViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    moons = Moon.objects.all().order_by('planet')
    queryset = Planet.objects.all().order_by('name')
    serializer_class = PlanetSerializer
    http_method_names = ['get']

    def retrieve(self, request, *args, **kwargs):
        try:
            planet = self.queryset.get(planet_id=kwargs['pk']).__dict__
            planet = PlanetSerializer(planet).data
            moons = self.moons.filter(planet=planet['planet_id'])
            planet['moons'] = list(moons.values())
            return Response(planet, status=status.HTTP_200_OK)
        except:
            return Response({}, status=status.HTTP_200_OK)

    def list(self, request, *args, **kwargs):
        result = []
        for planet in list(self.queryset.values()):
            moons = self.moons.filter(planet=planet['planet_id'])
            planet['moons'] = list(moons.values())
            result.append(planet)
        return Response(result, status=status.HTTP_200_OK)

    def create(self, request):
        response = {'message': 'Create function is not offered in this path.'}
        return Response(response, status=status.HTTP_403_FORBIDDEN)

    def update(self, request, pk=None):
        response = {'message': 'Update function is not offered in this path.'}
        return Response(response, status=status.HTTP_403_FORBIDDEN)

    def partial_update(self, request, pk=None):
        response = {'message': 'Update function is not offered in this path.'}
        return Response(response, status=status.HTTP_403_FORBIDDEN)

    def destroy(self, request, pk=None):
        response = {'message': 'Delete function is not offered in this path.'}
        return Response(response, status=status.HTTP_403_FORBIDDEN)


class MoonViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Moon.objects.all().order_by('planet')
    serializer_class = MoonSerializer
    http_method_names = ['get', 'post', 'put', 'delete']


@api_view(['GET'])
def reset_space(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        get_planets()
        return Response({"Hello": "World"}, status=status.HTTP_200_OK)
