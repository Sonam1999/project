from django.urls import path
from . import views

app_name="accounts"

urlpatterns=[
    path('signup/',views.sign_up,name="signup"),
    path('login/',views.log_in,name="login"),
    path('logout/',views.log_out,name="logout"),
]