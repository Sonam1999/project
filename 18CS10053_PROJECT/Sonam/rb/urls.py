from django.urls import path
from . import views

app_name='rb'
urlpatterns = [
    path('',views.br_room,name="home"),
    path('search/',views.br_search, name="search"),
    path('list/',views.br_list, name="list"),
    #path('<slug:slug>/',views.br_details, name="details"),
    path('book/<slug:slug>',views.room_book, name="book"),
    path('<slug:slug>/',views.br_details, name="details"),
    #path('book/',views.room_book, name="book"),
    #path('Search/',views.Search),
]
 