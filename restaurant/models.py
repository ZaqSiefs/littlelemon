from django.db import models
from django.core.validators import MaxValueValidator


# Create your models here.


class Booking(models.Model):
    ID = models.PositiveSmallIntegerField(primary_key=True, validators=[MaxValueValidator(11)])
    name = models.CharField(max_length=255)
    no_of_guests = models.PositiveSmallIntegerField(validators=[MaxValueValidator(6)])
    booking_date = models.DateTimeField()

    def __str__(self):
        return f"{self.name} | Guest Count: {self.no_of_guests} | Reservation: {self.booking_date}"
    
class Menu(models.Model):
    ID = models.PositiveSmallIntegerField(primary_key=True, validators=[MaxValueValidator(5)])
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    inventory = models.PositiveSmallIntegerField(validators=[MaxValueValidator(5)])
    
    def __str__(self):
        return f"{self.title} : ${str(self.price)}"
