from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('menu', views.menu, name='menu'),
    path('booking', views.booking, name='booking'),
    path('guest_details', views.guest_details, name='guest_details'),
]