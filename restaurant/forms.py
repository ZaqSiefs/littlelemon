from django import forms
from django.utils import timezone

class BookingForm(forms.Form):
    name = forms.CharField(max_length=100, help_text="Enter Your Name")
    no_of_guests = forms.IntegerField(max_value=15)
    booking_date = forms.DateField(initial=timezone.now().date())