from rest_framework import generics
from rest_framework.response import Response
from rest_framework.reverse import reverse
from drones import views


class ApiRootVersion2(generics.GenericAPIView):

    def get(self, request, *args, **kwargs):
        return Response({
            'vehicle-categories': request.build_absolute_uri(reverse(views.DroneCategoryList.name)),
            'vehicles': request.build_absolute_uri(reverse(views.DroneList.name)),
            'pilots': request.build_absolute_uri(reverse(views.PilotList.name)),
            'competitions': request.build_absolute_uri(reverse(views.CompetitionList.name))
        })
