from django.test import TestCase
from django.db import IntegrityError

from star.models import People, Specie, Planet, Starship, Film, Vehicle
from .data import people, species, planets, starships, films, vehicles, \
    people_many, species_many, planets_many, starships_many, films_many, vehicles_many


class StarshipTest(TestCase):
    """ Test module Starship for model """

    def setUp(self):
        planet1 = Planet.objects.create(**planets[0])
        planet2 = Planet.objects.create(**planets[1])

        Film.objects.create(**films[0])
        Film.objects.create(**films[1])

        People.objects.create(**people[0], homeworld=planet1)
        People.objects.create(**people[1], homeworld=planet2)

        self.ship1 = Starship.objects.create(**starships[0])
        self.ship1.pilots.set(starships_many[0]["pilots"])
        self.ship1.films.set(starships_many[0]["films"])

        self.ship2 = Starship.objects.create(**starships[1])
        self.ship2.pilots.set(starships_many[1]["pilots"])
        self.ship2.films.set(starships_many[1]["films"])

    def test_starship_attributes(self):
        self.assertEqual(self.ship1.name, "CR90 corvette")
        self.assertEqual(self.ship1.passengers, "600")
        self.assertEqual(len(self.ship1.pilots.all()), 1)
        self.assertEqual(len(self.ship1.films.all()), 2)

        self.assertEqual(self.ship2.name, "Star Destroyer")
        self.assertEqual(self.ship2.passengers, "n/a")
        self.assertEqual(len(self.ship2.pilots.all()), 2)
        self.assertEqual(len(self.ship2.films.all()), 1)
