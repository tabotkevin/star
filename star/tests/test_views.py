import json
from rest_framework import status
from django.test import TestCase
from rest_framework.test import APIClient

from star.models import People, Specie, Planet, Starship, Film, Vehicle

from .data import people, species, planets, starships, films, vehicles, \
    people_many, species_many, planets_many, starships_many, films_many, vehicles_many

# initialize the APIClient
client = APIClient()


class GetAllStarshipTest(TestCase):
    """ Test module for GET all Starships API """

    def setUp(self):
        self.planet1 = Planet.objects.create(**planets[0])
        self.planet2 = Planet.objects.create(**planets[1])

        self.film1 = Film.objects.create(**films[0])
        self.film2 = Film.objects.create(**films[1])

        People.objects.create(**people[0], homeworld=self.planet1)
        People.objects.create(**people[1], homeworld=self.planet2)

        self.ship1 = Starship.objects.create(**starships[0])
        self.ship1.pilots.set(starships_many[0]["pilots"])
        self.ship1.films.set(starships_many[0]["films"])

        self.ship2 = Starship.objects.create(**starships[1])
        self.ship2.pilots.set(starships_many[1]["pilots"])
        self.ship2.films.set(starships_many[1]["films"])

        self.ship_payload = starships[0]

    def test_get_all_starshipss(self):
        response = client.get("/star/starships/")
        self.assertEqual(len(response.data["results"]), 2)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_valid_single_starship(self):
        response = client.get(f"/star/starships/{self.ship1.id}/")
        self.assertEqual(response.data.get("id"), self.ship1.id)
        self.assertEqual(response.data.get("name"), "CR90 corvette")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_invalid_single_starship(self):
        response = client.get('/star/starships/30/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_create_starship(self):
        response = client.post('/star/starships/new',
                               data=json.dumps(self.ship_payload),
                               content_type='application/json'
                               )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_delete_starship(self):
        response = client.delete(f"/star/starships/{self.ship2.id}/")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_calc_evac_starship_id(self):
        response = client.get(
            f"/star/calc-evac/{self.ship1.id}/{self.planet1.id}/"
        )
        self.assertEqual(response.data.get("starships"), 334)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_calc_evac_starship_name(self):
        response = client.get(
            f"/star/calc-evac/{self.ship1.name}/{self.planet1.id}/"
        )
        self.assertEqual(response.data.get("starships"), 334)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
