from django.contrib import admin
from django.urls import path
from . import views 
urlpatterns = [
   
    path('<str:goal>',views.find_goal)
]