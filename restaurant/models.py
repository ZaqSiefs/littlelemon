from django.db import models
from django.core.validators import MaxValueValidator


# Create your models here.
    
class Menu(models.Model):
    ID = models.PositiveSmallIntegerField(primary_key=True, validators=[MaxValueValidator(100, "No more than 100 items on the menu.")])
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    inventory = models.PositiveSmallIntegerField(validators=[MaxValueValidator(200, "No more than 200 items in inventory.")])
    
    def __str__(self):
        return f"{self.title} : ${str(self.price)}"

class Booking(models.Model):
    
    ID = models.PositiveSmallIntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    no_of_guests = models.PositiveSmallIntegerField(validators=[MaxValueValidator(15, "Maximum of 15 guests.")])
    booking_date = models.DateTimeField()

    def __str__(self):
        return f"{self.name} | Guest Count: {self.no_of_guests} | Reservation: {self.booking_date}"