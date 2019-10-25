from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class City(models.Model):
    name = models.CharField(max_length=50)
    iata = models.CharField(max_length=10)


class Property(models.Model):
    # todo serch for numeric constraints
    address = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    daily_price = models.DecimalField(max_digits=13, decimal_places=2)
    image = models.CharField(max_length=200)
    max_pax = models.IntegerField()
    city = models.ForeignKey(City, on_delete=models.CASCADE)


class Host(User):
    pass


class Reservation(models.Model):
    total_price = models.DecimalField(max_digits=3, decimal_places=2)
    created_date = models.DateTimeField()


class RentalDate(models.Model):
    property = models.ForeignKey(Property, on_delete=models.CASCADE)
    reservation = models.ForeignKey(Reservation, on_delete=models.CASCADE)
    date = models.DateField()
