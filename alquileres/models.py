from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings


class City(models.Model):
    name = models.CharField(max_length=50)
    iata = models.CharField(max_length=10)

    class Meta : 
        verbose_name_plural = "Cities"

    def __str__(self):
        return self.name

class Host(AbstractUser):
    pass

class Property(models.Model):
    address = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    daily_price = models.DecimalField(max_digits=13, decimal_places=2)
    image = models.CharField(max_length=200)
    max_pax = models.IntegerField()
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    host = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)

    class Meta : 
        verbose_name_plural = "Properties"

    def __str__(self):
        return self.title

class Reservation(models.Model):
    total_price = models.DecimalField(max_digits=3, decimal_places=2)
    created_date = models.DateTimeField()


class RentalDate(models.Model):
    property = models.ForeignKey(Property, on_delete=models.CASCADE)
    reservation = models.ForeignKey(Reservation, on_delete=models.CASCADE, null=True)
    date = models.DateField()

    def __str__(self):
        return self.date.strftime('%d/%m/%Y')
