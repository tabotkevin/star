from django.contrib import admin
from .models import People, Specie, Planet, Starship, Film, Vehicle


@admin.register(
    People,
    Specie,
    Planet,
    Starship,
    Film,
    Vehicle
)
class ModelAdmin(admin.ModelAdmin):
    pass
