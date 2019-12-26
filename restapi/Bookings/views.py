from django.shortcuts import render
from rest_framework.viewsets import ViewSet, ModelViewSet
from rest_framework import status
from .serializers import Bookings_flightSerializer
from .models import Bookings_flight
from rest_framework.response import Response
from django.utils import timezone

class Bookings_flightViewSet(ModelViewSet):
    queryset = Bookings_flight.objects.all()
    serializer_class = Bookings_flightSerializer

    def create(self, request):

        obj = Bookings_flight()
        obj.userid = request.data['userid']
        obj.sectorcode = request.data['sectorcode']
        obj.sectorname = request.data['sectorname']
        obj.save()
        return Response({"message": "User input successful"}, status=status.HTTP_201_CREATED)
    

