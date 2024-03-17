from django.contrib import admin
from django.urls import path
from . import views 
urlpatterns = [
    # path('<int:mood_number>', views.find_mood_bynumber),
    # path('<str:mood_type>',views.find_mood, name = "mood_url"),
    # path('',views.mood_list),
    path('moods/', views.mood_list, name='mood-list'),
    path('expenses/', views.expense_list, name = 'expense-list'),
    path('goals/', views.goal_list, name = 'goal-list')
    
   
]