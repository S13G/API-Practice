from django.urls import reverse
from rest_framework import generics
from rest_framework.response import Response

from drones.models import Drone, DroneCategory, Pilot, Competition
from drones.serializers import DroneCategorySerializer, DroneSerializer, PilotSerializer, PilotCompetitionSerializer


# Create your views here.


class DroneCategoryList(generics.ListCreateAPIView):
    queryset = DroneCategory.objects.all()
    serializer_class = DroneCategorySerializer
    name = 'DroneCategory List'


class DroneCategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = DroneCategory.objects.all()
    serializer_class = DroneCategorySerializer
    name = 'dronecategory-detail'


class DroneList(generics.ListCreateAPIView):
    queryset = Drone.objects.all()
    serializer_class = DroneSerializer
    name = 'Drone List'


class DroneDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Drone.objects.all()
    serializer_class = DroneSerializer
    name = 'drone-detail'


class PilotList(generics.ListCreateAPIView):
    queryset = Pilot.objects.all()
    serializer_class = PilotSerializer
    name = 'Pilot List'


class PilotDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Pilot.objects.all()
    serializer_class = PilotSerializer
    name = 'pilot-detail'


class CompetitionList(generics.ListCreateAPIView):
    queryset = Competition.objects.all()
    serializer_class = PilotCompetitionSerializer
    name = 'Competition List'


class CompetitionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Competition.objects.all()
    serializer_class = PilotCompetitionSerializer
    name = 'competition-detail'


class ApiRoot(generics.GenericAPIView):

    def get(self, request, *args, **kwargs):
        return Response({
            'drone-categories': request.build_absolute_uri(reverse('DroneCategory List')),
            'drones': request.build_absolute_uri(reverse('Drone List')),
            'pilots': request.build_absolute_uri(reverse('Pilot List')),
            'competitions': request.build_absolute_uri(reverse('Competition List'))
        })