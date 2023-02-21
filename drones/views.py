from django.urls import reverse
from rest_framework import generics
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication

from drones.custom_permissions import IsCurrentUserOwnerOrReadOnly
from drones.filters import CompetitionFilter
from drones.models import Drone, DroneCategory, Pilot, Competition
from drones.serializers import DroneCategorySerializer, DroneSerializer, PilotSerializer, PilotCompetitionSerializer


# Create your views here.


class DroneCategoryList(generics.ListCreateAPIView):
    queryset = DroneCategory.objects.all()
    serializer_class = DroneCategorySerializer
    name = 'DroneCategory List'
    filter_fields = ('name',)
    ordering_fields = ('name',)
    search_fields = ('name',)


class DroneCategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = DroneCategory.objects.all()
    serializer_class = DroneCategorySerializer
    name = 'dronecategory-detail'


class DroneList(generics.ListCreateAPIView):
    queryset = Drone.objects.all()
    serializer_class = DroneSerializer
    name = 'Drone List'
    filter_fields = ('name', 'drone_category', 'manufacturing_date', 'has_it_completed',)
    search_fields = ('name',)
    ordering_fields = ('name', 'manufacturing_date',)
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsCurrentUserOwnerOrReadOnly)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class DroneDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Drone.objects.all()
    serializer_class = DroneSerializer
    name = 'drone-detail'
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsCurrentUserOwnerOrReadOnly)


class PilotList(generics.ListCreateAPIView):
    queryset = Pilot.objects.all()
    serializer_class = PilotSerializer
    name = 'Pilot List'
    filter_fields = ('name', 'gender', 'races_count',)
    search_fields = ('name',)
    ordering_fields = ('name', 'races_count',)
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)


class PilotDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Pilot.objects.all()
    serializer_class = PilotSerializer
    name = 'pilot-detail'
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)


class CompetitionList(generics.ListCreateAPIView):
    queryset = Competition.objects.all()
    serializer_class = PilotCompetitionSerializer
    name = 'Competition List'
    filter_class = CompetitionFilter
    ordering_fields = ('distance_in_feet', 'distance_achievement_date',)


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
