from django.contrib import admin
from drones.models import DroneCategory, Drone, Pilot, Competition
# Register your models here.

admin.site.register([DroneCategory, Drone, Pilot, Competition])
