from django.urls import path
from star.views import PeopleList, SpecieList, StarshipList, PlanetList, FilmList, VehicleList, StarshipCreate,\
    StarshipRetrieveUpdateDestroy, StarshipFilmSpecieList, FilmSpecieList, CalcEvac

urlpatterns = [
    path("people/", PeopleList.as_view(), name="people"),
    path("species/", SpecieList.as_view(), name="species"),
    path("planets/", PlanetList.as_view(), name="planets"),
    path("films/", FilmList.as_view(), name="films"),
    path("vehicles/", VehicleList.as_view(), name="vehicles"),
    path("starships/", StarshipList.as_view(), name="starships"),
    path('starships/new', StarshipCreate.as_view()),
    path('starships/<int:id>/',
         StarshipRetrieveUpdateDestroy.as_view(), name="starship"),
    path('search/<int:id>/', StarshipFilmSpecieList.as_view(), name="star-film"),
    path('search/<str:producer>/',
         FilmSpecieList.as_view(), name="film-specie"),
    path("calc-evac/<str:ship>/<int:planet_id>/",
         CalcEvac.as_view(), name="calc-evac"),
]
