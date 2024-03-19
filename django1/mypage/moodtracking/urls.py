from django.contrib import admin
from django.urls import path
from . import views 
urlpatterns = [
    # path('<int:mood_number>', views.find_mood_bynumber),
    # path('<str:mood_type>',views.find_mood, name = "mood_url"),
    # path('',views.mood_list),
    path('', views.index , name='index'),
    path('register/', views.register , name ='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('special/' , views.special, name='special'),
    path('moods/', views.mood_list, name='mood-list'),
    path('expenses/', views.expense_list, name = 'expense-list'),
    path('goals/', views.goal_list, name = 'goal-list'),
    path('goal-input/', views.goal_input, name = 'goal-input'),
    path('moods/<int:mood_id>', views.mood_detail, name='mood-detail'),
    path('expenses/<int:expense_id>', views.expense_detail, name='expense-detail'),
    path('goals/<int:goal_id>', views.goal_detail, name='goal-detail'),
    
   
]   