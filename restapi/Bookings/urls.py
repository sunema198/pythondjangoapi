from rest_framework.routers import DefaultRouter
from django.conf.urls import include, url
from .views import Bookings_flightViewSet

router = DefaultRouter()
router.register("Bookings_Flight", Bookings_flightViewSet,
                basename='Bookings_flight')

urlpatterns = [
    url('',include(router.urls))
]
