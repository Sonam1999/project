from django.http import HttpResponse
from django.shortcuts import render
def homepage(request):
    return render(request,'homepage.html')
def Sign_up(request):
    return render(request,'Sign_up.html')
def Search(request):
    return render(request,'Search.html')