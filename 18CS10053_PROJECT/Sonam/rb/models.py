from django.db import models,migrations
from django.contrib.auth.models import User
from multiselectfield import MultiSelectField
#from django.template.defaultfilters import slugify

class Hotel(models.Model):
    AMENITIES =(
        ('AC','AC'),
        ('TV','TV'),
        ('Kitchen','Kitchen'),
        ('Free Wifi','Free Wifi'),
        ('Mini Fridge','Mini Fridge'),
        ('Power Backup','Power Backup'),
        ('Geyser','Geyser'),
        ('Parking Facility','Parking Facility'),
        ('Card Payment','Card Payment'),
        ('CCTV Camera','CCTV Camera'),
        ('Daily Housekeeping','Daily Housekeeping'),
        ('24/7 CheckIn','24/7 CheckIn'),
        ('Coffee/Tea Maker','Coffee/Tea Maker'),
        ('Fan','Fan'),
    )
    CATEGORY =(
        ('Single Room','Single Room'),
        ('Double Sharing','Double Sharing'),
        ('Triple Sharing','Triple Sharing'),
        ('Room for 4','Room for 4'),
            )
    STATUS =(
        ('Room Available','Room Available'),
        ('Room Unavailable','Room Unavailable'),
            )
    name=models.CharField(max_length=100,null=True)
    desc=models.TextField(null=True)
    location=models.CharField(max_length=50,null=True)
    mobile=models.IntegerField(max_length=11,null=True)
    address=models.TextField(null=True)
    slug=models.CharField(max_length=100, null=True)
    HotelPolicy=models.TextField(null=True)
    price=models.FloatField(null=True)
    category=MultiSelectField(max_length=100,null=True,choices=CATEGORY)
    amenities=MultiSelectField(max_length=300,null=True,choices=AMENITIES)
    status=models.CharField(max_length=100,null=True,choices=STATUS)
    thumb1=models.ImageField(max_length=100,default='default.png')
    thumb2=models.ImageField(max_length=100,default='default.png')
    thumb3=models.ImageField(max_length=100,default='default.png')
    thumb4=models.ImageField(max_length=100,default='default.png')   
    thumb5=models.ImageField(max_length=100,default='default.png')
    thumb6=models.ImageField(max_length=100,default='default.png')
    thumb7=models.ImageField(max_length=100,default='default.png')
    thumb8=models.ImageField(max_length=100,default='default.png') 
    thumb9=models.ImageField(max_length=100,default='default.png')
    thumb10=models.ImageField(max_length=100,default='default.png')
    thumb11=models.ImageField(max_length=100,default='default.png')    
    author=models.ForeignKey(User,default=None,on_delete=models.CASCADE)
    def __str__(self):
    	return self.name
    def snippet(self):
        return self.desc

class Booking(models.Model):
    user=models.ForeignKey(User,null=True, on_delete=models.SET_NULL)
    hotel=models.ForeignKey(Hotel,null=True, on_delete=models.SET_NULL)
    date_of_Booking=models.DateTimeField(auto_now_add=True,null=True)

    # form inputs
    cust_Name=models.CharField(max_length=100,null=True)
    phone=models.CharField(max_length=100,null=True)
    email=models.CharField(max_length=100,null=True)
    location=models.CharField(max_length=100,null=True)
    checkIn=models.DateTimeField(null=True)
    checkOut=models.DateTimeField(null=True)
    guest=models.IntegerField(null=True)
    def __str__(self):
        return self.cust_Name
