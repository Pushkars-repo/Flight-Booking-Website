from django.db import models

# Create your models here.





class Flight(models.Model):
    origin = models.CharField(max_length=64)
    destination = models.CharField(max_length=64)
    depart_time = models.TimeField(auto_now=False, auto_now_add=False)
    arrival_time = models.TimeField(auto_now=False, auto_now_add=False)
    plane = models.CharField(max_length=24)
    airline = models.CharField(max_length=64)
    origin_airport=models.CharField(max_length=500, default='')
    destination_airport=models.CharField(max_length=500, default='')
    fare = models.FloatField(null=True)
    airline_logo = models.ImageField(upload_to='uploaded', null=True)

    def __str__(self):
        return f"{self.id}: {self.origin} to {self.destination}"


