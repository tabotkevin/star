from rest_framework.exceptions import ValidationError
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveUpdateDestroyAPIView, GenericAPIView
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.response import Response
from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404
import math


from .serializers import PeopleSerializer, SpecieSerializer, PlanetSerializer, StarshipSerializer, FilmSerializer, \
    VehicleSerializer, StarshipFilmSpecieSerializer, FilmSpecieSerializer
from .models import People, Specie, Planet, Starship, Film, Vehicle


class ModelPagination(LimitOffsetPagination):
    default_limit = 5
    max_limit = 100


# -------------------  Starship search Views ----------------------------------
class StarshipFilmSpecieList(GenericAPIView):
    lookup_field = "id"
    serializer_class = StarshipFilmSpecieSerializer
    queryset = Starship.objects.all()

    def get(self, request, *args, **kwargs):
        result = {}
        starship = self.get_object()
        for film in starship.films.all():
            result[film.title] = [
                SpecieSerializer(specie).data for specie in film.species.all()
            ]
        result = {
            starship.name: result
        }
        serializer = StarshipFilmSpecieSerializer({
            "starship_result": result
        })

        return Response(serializer.data)


class FilmSpecieList(GenericAPIView):
    queryset = Film.objects.all()

    def get(self, request, *args, **kwargs):
        result = {}
        films = self.queryset.filter(
            producer__icontains=self.kwargs["producer"]
        )
        for film in films:
            result[film.title] = [
                SpecieSerializer(specie).data for specie in film.species.all()
            ]
        serializer = FilmSpecieSerializer({
            "film_result": result
        })

        return Response(serializer.data)


class CalcEvac(GenericAPIView):

    def get(self, request, *args, **kwargs):
        result = {}
        try:
            ship = self.kwargs["ship"]

            starship = Starship.objects.get(id=int(ship)) if ship.isdigit(
            ) else Starship.objects.get(name=ship)

            planet = Planet.objects.get(id=self.kwargs["planet_id"])
            if planet.population is None or starship.passengers is None:
                raise ValidationError(
                    {'error': 'Empty fields for Population or passenger'}
                )
            result["starships"] = math.ceil(
                int(planet.population) / int(starship.passengers)
            )
        except ValueError:
            raise ValidationError(
                {'error': 'A valid starship-id and planet-id is required'})
        except TypeError:
            raise ValidationError(
                {'error': 'Type error for Population or passenger field(s)'})
        except ObjectDoesNotExist:
            raise(Http404)
        return Response(result)


# -------------------  Starship CRUD Views ----------------------------------
class StarshipList(ListAPIView):
    queryset = Starship.objects.all()
    serializer_class = StarshipSerializer
    filter_backends = (DjangoFilterBackend, SearchFilter)
    filter_fields = ("id",)
    search_fields = ("name",)
    pagination_class = ModelPagination


class StarshipCreate(CreateAPIView):
    serializer_class = StarshipSerializer


class StarshipRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    queryset = Starship.objects.all()
    lookup_field = 'id'
    serializer_class = StarshipSerializer


# -------------------  List view for the rest of the other models ----------------------------------

class PeopleList(ListAPIView):
    queryset = People.objects.all()
    serializer_class = PeopleSerializer
    filter_backends = (DjangoFilterBackend, SearchFilter)
    filter_fields = ("id",)
    search_fields = ("name",)
    pagination_class = ModelPagination


class SpecieList(ListAPIView):
    queryset = Specie.objects.all()
    serializer_class = SpecieSerializer
    filter_backends = (DjangoFilterBackend, SearchFilter)
    filter_fields = ("id",)
    search_fields = ("name",)
    pagination_class = ModelPagination


class PlanetList(ListAPIView):
    queryset = Planet.objects.all()
    serializer_class = PlanetSerializer
    filter_backends = (DjangoFilterBackend, SearchFilter)
    filter_fields = ("id",)
    search_fields = ("name",)
    pagination_class = ModelPagination


class FilmList(ListAPIView):
    queryset = Film.objects.all()
    serializer_class = FilmSerializer
    filter_backends = (DjangoFilterBackend, SearchFilter)
    filter_fields = ("id",)
    search_fields = ("title",)
    pagination_class = ModelPagination


class VehicleList(ListAPIView):
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer
    filter_backends = (DjangoFilterBackend, SearchFilter)
    filter_fields = ("id",)
    search_fields = ("name",)
    pagination_class = ModelPagination
