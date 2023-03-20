# pigello

PlanetaryPlay API

A pointless system that lets users add and remove solar system objects that orbits planets – relative to our actual solar system.

General Information

The system will keep track of the “custom solar system” – and will be able to return information about it, as well as allow manipulation of which bodies orbits which planets.

The “custom solar system” will always have our real solar system as a base, as a startingpoint, as a reference point.

The “custom solar system” is shared with all users of the API, it’s anonymous and does not use any authentication.

To get information about our real solar system, the Solar System openData – API should be used (swagger doc url: https://api.le-systeme-solaire.net/rest/). This endpoint doesn’t require authentication.

It is fine to use another API that can be used to represent our actual solar system

Functional Description

· A user of PlanetaryPlay can’t modify anything about planets, they can’t modify which planets exists or any other information about the planet. In other words, our real solar system dictates which planets exists.

· A user of PlanetaryPlay should be able to see which planets exists, and which bodies orbits those planets, in the “custom solar system”.

o Information about a planet should at least contain information about it’s: Name, Mass, Gravity Constant, Volume

o Information about an orbiting body should at least contain information about it’s: Name, Mass, Gravity Constant, Volume

· A user of PlanetaryPlay should be able to add a new body that orbits a given planet.

· A user of PlanetaryPlay should be able to remove a body that orbits a given planet, including bodies that is not added by the users of PlanetaryPlay, but that exists in our real solar system.

· A user of PlanetaryPlay should be able to modify any given body that orbits a planet.

· A user of PlanetaryPlay should be able to (directly from the backends responses) see the total mass, volume and density of all bodies, including the plantes, around a given/provided set of planets.

Note – you must implement all solutions, no pseudo code or template code.

Practical Information

A REST API will be written.

The backend will be written in python 3.8, with Django and Django Rest Framework.

Django: https://www.djangoproject.com Django Rest Framework: https://www.django-rest-framework.org

The project’s starting point is prepared (with some examples if you happen to be unfamiliar with Django), you can find its repo here: https://github.com/Pigello/backend-test

To get started, create a python environment (if you call it “py_env” it’s already git-ignored), located at the root of the project, then install the minimum required dependencies with the help of the requirements.txt file located in the repo.

Recommended time for this test is ≈90 minutes.

When done – publish your solution to github and invite the github user with username “toranderr” to view the repository.

Django specific Information

After any modification to database models, generate migration files with python manage.py makemigrations

To apply migrations, run python manage.py migrate

To run server, run python manage.py runserver
