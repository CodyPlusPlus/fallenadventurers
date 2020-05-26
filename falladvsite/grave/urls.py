from django.contrib import admin
from django.urls import path, include 
from . import views

urlpatterns = [
    path('', views.home, name='grave-home'),
    path('about/', views.about, name='grave-about'),
    path('explore/', views.explore, name='grave-explore'),
    path('newgrave/', views.newgrave, name='grave-new')
]
