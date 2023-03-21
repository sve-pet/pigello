import json

import requests

from planetary_play.models import Planet, Moon


def get_planets():
    response = requests.get("https://api.le-systeme-solaire.net/rest.php/bodies")
    solar_system = json.loads(response.text)

    for body in solar_system['bodies']:

        if body['mass'] and body['mass']['massValue']:
            mass = body['mass']['massValue']
        else:
            mass = 0.0

        if body['vol'] and body['vol']['volValue']:
            vol = body['vol']['volValue']
        else:
            vol = 0.0

        if body['isPlanet']:
            planet = Planet(
                planet_id=body['id'],
                name=body['name'],
                mass=mass,
                vol=vol,
                gravity=body['gravity']
            )
            planet.save()
        elif body['aroundPlanet']:
            moon = Moon(
                moon_id=body['id'],
                name=body['name'],
                mass=mass,
                vol=vol,
                gravity=body['gravity'],
                planet=body['aroundPlanet']['planet']
            )
            moon.save()

    return response
