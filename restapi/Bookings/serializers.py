from rest_framework import serializers
from .models import Bookings_flight

class Bookings_flightSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bookings_flight
        fields = '__all__'