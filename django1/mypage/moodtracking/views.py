from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
# Create your views here.

moods_dict = {
    "happy":"This is the happy mood",
    "sad":"This is the sad mood!"
}
def find_mood_bynumber(request, mood_number):
    
    moods_list = list(moods_dict.keys())
    
    if len(moods_list) <mood_number:
        return HttpResponseNotFound("Invalid request") 
    redirect_mood = moods_list[mood_number-1]
    redirect_path = reverse("mood_url", args = [redirect_mood])
    return HttpResponseRedirect(redirect_path)
    

def find_mood(request, mood_type):
    
    try:
       mood_text  = moods_dict[mood_type] 
    
    except:
      return HttpResponseNotFound()
       
    return HttpResponse(mood_text)

def find_goal(request,goal):
    return HttpResponse(f"this is the goal page for:  {goal}")

# def mood_bynumber1(request,mood_number):
#     mood_list = list(moods_dict.keys())
#     mood_redirect= mood_list[mood_number]
    
#     return HttpResponseRedirect("/moods"+ mood_redirect)

## -------------
# goals

