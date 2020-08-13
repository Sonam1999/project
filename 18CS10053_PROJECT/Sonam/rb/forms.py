from django import forms
from . import models
import datetime
from .models import Hotel,Booking
from crispy_forms.helper import FormHelper

LOCATION_CHOICES=(
    ('Delhi','Delhi'),
    ('Mumbai','Mumbai'),
    ('Kolkata','Kolkata'),
    ('Jaipur','Jaipur'),
    ('Udaipur','Udaipur'),
    ('Hyderabad','Hyderabad'),
    ('Kashmir','Kashmir'),
    ('Chandigarh','Chandigarh'),
    ('Noida','Noida'),
)
class BookRoom(forms.ModelForm):
    class Meta:
        model=models.Hotel
        fields={'name','slug','location'}

class HotelForm(forms.ModelForm):
    title=forms.CharField(max_length=100)
    body=forms.CharField(max_length=100,label="Item Description")

    class Meta:
        model= Hotel
        fields=('title','body',)

class booking_form(forms.Form):
    name = forms.CharField()
    phone = forms.IntegerField()
    email = forms.EmailField()
    number_of_guest = forms.IntegerField()
    checkin_date = forms.DateTimeField(label='Check-In Date',widget=forms.DateTimeInput(
    attrs={
        'placeholder':'YYYY-MM-DD HH:MM'
        }
    ))
    checkout_date = forms.DateTimeField(label='Check-Out Date',widget=forms.DateTimeInput(
    attrs={
        'placeholder':'YYYY-MM-DD HH:MM'
        }
    ))
    date_of_booking = forms.DateField(widget=forms.DateTimeInput(
    attrs={
        'placeholder':'DD/MM/YYYY'
        }
    ))

       

class searching_form(forms.Form):
    location = forms.CharField(label='LOCATION', widget=forms.Select(choices=LOCATION_CHOICES))
    checkin = forms.DateTimeField(label='Check-In Date',widget=forms.DateTimeInput(
    attrs={
        'placeholder':'YYYY-MM-DD HH:MM'
        }
    ))
    checkout = forms.DateTimeField(label='Check-Out Date',widget=forms.DateTimeInput(
    attrs={
        'placeholder':'YYYY-MM-DD HH:MM'
        }
    ))
    number_of_guest = forms.IntegerField(label='Number of Guests')


  


