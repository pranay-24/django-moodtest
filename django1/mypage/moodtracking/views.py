from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
# Create your views here.

def find_mood_bynumber(request, mood_number):
    mood_text = None
    
    if mood_number ==1:
        mood_text = 'Happy'
    elif mood_number ==2:
        mood_text = 'Sad'
    else:
        return HttpResponseNotFound()
    return HttpResponse(mood_text)

def find_mood(request, mood_type):
    mood_text  = None
    
    if mood_type =='happy':
        mood_text = 'Happy'
    elif mood_type =='sad':
        mood_text = 'Sad'
    else:
        return HttpResponseNotFound()
    return HttpResponse(mood_text)