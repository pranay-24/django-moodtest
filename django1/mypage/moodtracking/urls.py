from django.contrib import admin
from django.urls import path
from . import views 
urlpatterns = [
    path('<int:mood_number>', views.find_mood_bynumber),
    path('<str:mood_type>',views.find_mood, name = "mood_url"),
   
]