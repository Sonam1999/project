from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Hotel,Booking
from django.contrib.auth.decorators import login_required
from .forms import booking_form,searching_form
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login,logout
# Create your views here.
def sign_up(request):
    if request.method=='POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user=form.save()
            login(request,user)
            return redirect('accounts:login')
    else: 
        form = UserCreationForm()
    return render(request,'accounts/signup.html',{'form':form})

def br_room(request):
    return render(request,'rb/br_home.html')

def br_list(request):          
    return render(request,'rb/br_list.html')    

def br_details(request,slug):
    title= Hotel.objects.get(slug=slug)
    return render(request,'rb/br_details.html',{'title':title})

@login_required(login_url="/accounts/login/")
def room_book(request,slug):
    title = Hotel.objects.get(slug=slug)

    if request.method=='POST':
        print(request.POST)
        form = booking_form(request.POST)
        if form.is_valid():
            book_obj = Booking()

            # booking object
            book_obj.cust_Name = form.data['name']
            book_obj.phone = form.data['phone']
            book_obj.email = form.data['email']
            book_obj.guest = form.data['number_of_guest']
            book_obj.checkIn = form.data['checkin_date']
            book_obj.checkOut = form.data['checkout_date']
            
            book_obj.user = request.user
            book_obj.hotel = title
            book_obj.location=title.location
            
            book_obj.save()
           

            return render(request,'rb/confirm.html',{'form':book_obj})
        else:
            return render(request,'rb/book_room.html',{'form':form, 'title':title})
    else:   
        form = booking_form()
        return render(request,'rb/book_room.html',{'form':form, 'title':title})
#request.POST,request.FILES

def bconfirm(request):
    if request.method == 'POST':
        return render(request,'rb/confirm.html')

def br_search(request):
    if request.method=='POST':
        print(request.POST)
        form = searching_form(request.POST)
        results=[]
        for hotel in Hotel.objects.all():
            if hotel.location==form.data['location']:
                results.append(hotel)

        return render(request,'rb/br_list.html',{'results':results})
    else:   
        form = searching_form()
        return render(request,'rb/br_search.html',{'form':form})
#request.POST,request.FILES
