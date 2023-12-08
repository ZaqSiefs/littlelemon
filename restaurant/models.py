from django.db import models
from django.core.validators import MaxValueValidator


# Create your models here.
    
class Menu(models.Model):
    ID = models.PositiveSmallIntegerField(primary_key=True, validators=[MaxValueValidator(100)])
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    inventory = models.PositiveSmallIntegerField(validators=[MaxValueValidator(200)])
    
    def __str__(self):
        return f"{self.title} : ${str(self.price)}"

class Booking(models.Model):
    
    ID = models.PositiveSmallIntegerField(primary_key=True, validators=[MaxValueValidator(24)]) # Let's say there are a maximum of 24 tables
    name = models.CharField(max_length=255)
    no_of_guests = models.PositiveSmallIntegerField(validators=[MaxValueValidator(15)])
    booking_date = models.DateTimeField()

    def __str__(self):
        return f"{self.name} | Guest Count: {self.no_of_guests} | Reservation: {self.booking_date}"