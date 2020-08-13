from django.contrib import admin
from django.urls import path, include
from .import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings
from rb import views as rb_views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/',include('accounts.urls')),
    path('rb/',include('rb.urls')),
    path('',rb_views.br_room,name="home"),
    path('',rb_views.br_list,name="list"),
    path('',rb_views.bconfirm,name="confirm"),
    path('Sign_up/',views.Sign_up),
    path('Search/',views.Search),
]
urlpatterns+=staticfiles_urlpatterns()
urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
