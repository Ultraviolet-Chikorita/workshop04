from django.contrib import admin
from .models import Person, Pet, SpiritAnimal, PlacesVisited, BirthCertificate

# Register your models here.
admin.site.register(Person)

admin.site.register(Pet)

admin.site.register(SpiritAnimal)

admin.site.register(PlacesVisited)

admin.site.register(BirthCertificate)