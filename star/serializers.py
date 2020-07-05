from rest_framework import serializers
from .models import People, Specie, Planet, Starship, Film, Vehicle


class StarshipSerializer(serializers.ModelSerializer):
    url = serializers.CharField(read_only=True)

    class Meta:
        model = Starship
        exclude = ()


class SpecieSerializer(serializers.ModelSerializer):
    url = serializers.CharField(read_only=True)

    class Meta:
        model = Specie
        exclude = ()


class FilmSerializer(serializers.ModelSerializer):
    url = serializers.CharField(read_only=True)

    class Meta:
        model = Film
        exclude = ()


class PeopleSerializer(serializers.ModelSerializer):
    url = serializers.CharField(read_only=True)

    class Meta:
        model = People
        exclude = ()


class PlanetSerializer(serializers.ModelSerializer):
    url = serializers.CharField(read_only=True)

    class Meta:
        model = Planet
        exclude = ()


class VehicleSerializer(serializers.ModelSerializer):
    url = serializers.CharField(read_only=True)

    class Meta:
        model = Vehicle
        exclude = ()


class StarshipFilmSpecieSerializer(serializers.Serializer):
    starship_result = serializers.DictField(
        serializers.DictField(
            child=serializers.ListField(
                child=SpecieSerializer(),
            )
        )
    )


class FilmSpecieSerializer(serializers.Serializer):
    film_result = serializers.DictField(
        child=serializers.ListField(
            child=serializers.DictField(),
        )
    )
