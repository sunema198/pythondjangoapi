from django.db import models

class Bookings_flight(models.Model):
    
    userid = models.CharField(max_length=50)
    sectorcode = models.CharField(max_length=50)
    sectorname = models.CharField(max_length=100)

    def __str__(self):
        return self.sectorname
    