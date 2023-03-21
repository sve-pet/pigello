import json

from django.test import TestCase

from planetary_play.models import Moon, Planet

# test data
test_moons = [{
    "name": "The Moon",
    "vol": 2.2,
    "gravity": 2.3,
    "planet": "earth",
    "mass": 1.0,
    "moon_id": "moon"
},
    {
        "name": "Another Moon",
        "vol": 2.2,
        "gravity": 2.3,
        "planet": "pluto",
        "mass": 1.0,
        "moon_id": "amoon"
    },
    {
        "name": "Yet Another Moon",
        "vol": 2.2,
        "gravity": 2.3,
        "planet": "pluto",
        "mass": 1.0,
        "moon_id": "yamoon"
    }
]

test_planets = [{
    "name": "Earth",
    "vol": 2.2,
    "gravity": 2.3,
    "mass": 1.0,
    "planet_id": "earth"
},
    {
        "name": "Pluto",
        "vol": 2.2,
        "gravity": 2.3,
        "mass": 1.0,
        "planet_id": "pluto"
    },
    {
        "name": "Findus",
        "vol": 2.2,
        "gravity": 2.3,
        "mass": 1.0,
        "planet_id": "findus"
    }
]


class ProductTestCase(TestCase):

    def setUp(self):
        # create instance of model
        for test_moon in test_moons:
            moon = Moon(**test_moon)
            moon.save()

        for test_planet in test_planets:
            planet = Planet(**test_planet)
            planet.save()

    def test_product_database(self):
        moon = Moon.objects.get(moon_id="moon")
        self.assertEqual(moon.name, "The Moon")

        planet = Planet.objects.get(planet_id="earth")
        self.assertEqual(planet.name, "Earth")

    def test_product_get_all_planets(self):
        response = self.client.get('/planets', follow=True)
        response = json.loads(response.content.decode("utf-8"))
        self.assertEqual(len(response), 3)

    def test_product_get_all_moons(self):
        response = self.client.get('/moons', follow=True)
        response = json.loads(response.content.decode("utf-8"))
        self.assertEqual(len(response), 3)
