from django.db import models


class Moon(models.Model):
    moon_id = models.CharField(primary_key=True, max_length=20)
    name = models.CharField(max_length=20)
    vol = models.DecimalField(max_digits=10, decimal_places=2)
    gravity = models.DecimalField(max_digits=10, decimal_places=2)
    planet = models.CharField(max_length=20)
    mass = models.DecimalField(max_digits=10, decimal_places=2)


class Planet(models.Model):
    planet_id = models.CharField(primary_key=True, max_length=20)
    name = models.CharField(max_length=20)
    vol = models.DecimalField(max_digits=10, decimal_places=2)
    gravity = models.DecimalField(max_digits=10, decimal_places=2)
    mass = models.DecimalField(max_digits=10, decimal_places=2)

# Create your models here.
