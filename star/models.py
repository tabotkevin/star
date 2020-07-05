from django.db import models
from functools import partial

from django.utils import timezone
from django.db import models
from django.conf import settings


class BaseModel:
    URL = f"{settings.HOSTNAME}/star"

    def url(self):
        return "{}/{}/{}/".format(self.URL, self._meta.db_table, self.id)

    def repr(self, attr):
        return '<{} ({}) "{}">'.format(self.__class__.__name__, self.id, attr)


class People(BaseModel, models.Model):
    GENDER_CHOICES = (
        ("Male", "Male"),
        ("Female", "Female"),
        ("unknown", "unknown"),
        ("n/a", "n/a")
    )

    name = models.CharField(max_length=50, blank=True, null=True)
    birth_year = models.CharField(max_length=10, blank=True, null=True)
    eye_color = models.CharField(max_length=50, blank=True, null=True)
    gender = models.CharField(
        max_length=10, choices=GENDER_CHOICES, blank=True, null=True)
    hair_color = models.CharField(max_length=50, blank=True, null=True)
    height = models.CharField(max_length=50, blank=True, null=True)
    mass = models.CharField(max_length=50, blank=True, null=True)
    skin_color = models.CharField(max_length=50, blank=True, null=True)
    homeworld = models.OneToOneField(
        "Planet", on_delete=models.CASCADE, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    edited = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    films = models.ManyToManyField("Film", blank=True)
    species = models.ManyToManyField(
        "Specie", related_name="specie", blank=True)
    starships = models.ManyToManyField("Starship", blank=True)
    vehicles = models.ManyToManyField("Vehicle", blank=True)

    class Meta:
        db_table = "people"

    def __repr__(self):
        return super(People, self).repr(self.name)


class Film(BaseModel, models.Model):
    title = models.CharField(max_length=100, blank=True, null=True)
    episode_id = models.IntegerField(blank=True, null=True)
    opening_crawl = models.TextField(blank=True, null=True)
    director = models.CharField(max_length=50, blank=True, null=True)
    producer = models.CharField(max_length=50, blank=True, null=True)
    release_date = models.DateTimeField(
        auto_now_add=True, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    edited = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    species = models.ManyToManyField("Specie", blank=True)
    starships = models.ManyToManyField("Starship", blank=True)
    vehicles = models.ManyToManyField("Vehicle", blank=True)
    characters = models.ManyToManyField(People, blank=True)
    planets = models.ManyToManyField("Planet", blank=True)

    class Meta:
        db_table = "films"

    def __repr__(self):
        return super(Film, self).repr(self.title)


class Planet(BaseModel, models.Model):
    name = models.CharField(max_length=50, blank=True, null=True)
    diameter = models.CharField(max_length=50, blank=True, null=True)
    rotation_period = models.CharField(max_length=50, blank=True, null=True)
    orbital_period = models.CharField(max_length=50, blank=True, null=True)
    gravity = models.CharField(max_length=50, blank=True, null=True)
    population = models.CharField(max_length=100, blank=True, null=True)
    climate = models.CharField(max_length=50, blank=True, null=True)
    terrain = models.CharField(max_length=200, blank=True, null=True)
    surface_water = models.CharField(max_length=50, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    edited = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    residents = models.ManyToManyField(People, blank=True)
    films = models.ManyToManyField(Film, blank=True)

    class Meta:
        db_table = "planets"

    def __repr__(self):
        return super(Planet, self).repr(self.name)


class Starship(BaseModel, models.Model):
    name = models.CharField(max_length=50, blank=True, null=True)
    model = models.CharField(max_length=50, blank=True, null=True)
    starship_class = models.CharField(max_length=50, blank=True, null=True)
    manufacturer = models.CharField(max_length=100, blank=True, null=True)
    cost_in_credits = models.CharField(max_length=50, blank=True, null=True)
    length = models.CharField(max_length=100, blank=True, null=True)
    crew = models.CharField(max_length=50, blank=True, null=True)
    passengers = models.CharField(max_length=200, blank=True, null=True)
    max_atmosphering_speed = models.CharField(
        max_length=50, blank=True, null=True)
    hyperdrive_rating = models.CharField(max_length=50, blank=True, null=True)
    MGLT = models.CharField(max_length=100, blank=True, null=True)
    cargo_capacity = models.CharField(max_length=50, blank=True, null=True)
    consumables = models.CharField(max_length=100, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    edited = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    pilots = models.ManyToManyField(People, blank=True)
    films = models.ManyToManyField(Film, blank=True)

    class Meta:
        db_table = "starships"

    def __repr__(self):
        return super(Starship, self).repr(self.name)


class Specie(BaseModel, models.Model):
    name = models.CharField(max_length=50, blank=True, null=True)
    classification = models.CharField(max_length=50, blank=True, null=True)
    designation = models.CharField(max_length=50, blank=True, null=True)
    average_height = models.CharField(max_length=50, blank=True, null=True)
    average_lifespan = models.CharField(max_length=50, blank=True, null=True)
    eye_colors = models.CharField(max_length=100, blank=True, null=True)
    hair_colors = models.CharField(max_length=50, blank=True, null=True)
    skin_colors = models.CharField(max_length=50, blank=True, null=True)
    language = models.CharField(max_length=50, blank=True, null=True)
    homeworld = models.CharField(max_length=50, blank=True, null=True)
    people = models.CharField(max_length=100, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    edited = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    people = models.ManyToManyField(People, blank=True)
    films = models.ManyToManyField(Film, blank=True)

    class Meta:
        db_table = "species"

    def __repr__(self):
        return super(Specie, self).repr(self.name)


class Vehicle(BaseModel, models.Model):
    name = models.CharField(max_length=50, blank=True, null=True)
    model = models.CharField(max_length=50, blank=True, null=True)
    vehicle_class = models.CharField(max_length=50, blank=True, null=True)
    manufacturer = models.CharField(max_length=100, blank=True, null=True)
    cost_in_credits = models.CharField(max_length=50, blank=True, null=True)
    length = models.CharField(max_length=100, blank=True, null=True)
    crew = models.CharField(max_length=50, blank=True, null=True)
    passengers = models.CharField(max_length=200, blank=True, null=True)
    max_atmosphering_speed = models.CharField(
        max_length=50, blank=True, null=True)
    cargo_capacity = models.CharField(max_length=50, blank=True, null=True)
    consumables = models.CharField(max_length=100, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    edited = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    pilots = models.ManyToManyField(People, blank=True)
    films = models.ManyToManyField(Film, blank=True)

    class Meta:
        db_table = "vehicles"

    def __repr__(self):
        return super(Vehicle, self).repr(self.name)
