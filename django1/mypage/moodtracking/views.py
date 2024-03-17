from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string
from .models import Mood, Goal
from forms import MoodFormm ,GoalForm
# Create your views here.

moods_list = [
    {"mood_title":"happy" , "description":"This is the happy mood"},
    {"mood_title":"sad" , "description":"This is the sad mood"}
]
#using list comprehension, create list of moods, use reverse to create redirect path, then redirect
def find_mood_bynumber(request, mood_number):
    
    #moods_list = list(moods_dict.keys())
    moods = [mood['mood_title'] for mood in moods_list]
    
    if len(moods_list) <mood_number:
        return HttpResponseNotFound("Invalid request") 
    redirect_mood = moods[mood_number-1]
    redirect_path = reverse("mood_url", args = [redirect_mood])
    #return HttpResponseRedirect(redirect_path)
    return HttpResponseRedirect(redirect_path)
    
#show mood detail
def find_mood(request, mood_type):
    
       try:
        #mood_text  = moods_dict[mood_type] 
        filtered_mood = next(mood for mood in moods_list if mood_type == mood['mood_title'].lower() )
#       return HttpResponse(mood_text)
        # response_data = render_to_string("moodtracking/moodtracking.html")
        # return HttpResponse(response_data)
        return render(request, "moodtracking/moodDetail.html", {"mood_type":mood_type.capitalize(), "mood_text":filtered_mood['description']})
       except:
           return HttpResponseNotFound("This mood does not exist")

#list of moods
def mood_list (request):
       
       moods = [ mood['mood_title'] for mood in moods_list]
       moodPage = ""
 
    #    for mood in moods_list:
    #        moodPage += f'<li><a href={reverse("mood_url", args = [mood])}>{mood}</a></li>'
       
    #    return HttpResponse(moodPage)
       return render(request, "moodtracking/moodList.html",{"mood_list":moods}) 
   
def find_goal(request,goal):
    return HttpResponse(f"this is the goal page for:  {goal}")

# def mood_bynumber1(request,mood_number):
#     mood_list = list(moods_dict.keys())
#     mood_redirect= mood_list[mood_number]
    
#     return HttpResponseRedirect("/moods"+ mood_redirect)

## -------------
# goals

##------
# filtering Syntax
# next(  post for post in posts if post['slug']== slug )

def create_mood (request):
    new_mood = Mood.objects.create(mood_name = ,   description = , url = )
    return render(request, "",{"new_mood" = new_mood } )

def mood_input(request):
    if request == 'POST':
        form = MoodForm(request.POST)
        
        if form.isValid():
            mood_name = form.clean_data['mood_name']
            description = form.cleaned_data['description']
            new_mood = Mood.objects.create(mood_name = mood_name,   description = description)
            return redirect('moodlist.html')
    else :
        form =  MoodForm()
    return render(request,'moodinput.html', {'form':form})
def find_mood(request, mood_id):
    mood = Mood.objects.filter(id= mood_id)
    return render(request, "", {"mood":mood})

def find_moods(request):
    moods = Mood.objects.all()
    return render(request,"", {"moods":moods})

#creating view function to input the goal
#errors solved - is_valid(), request.method == POST, form(request.POST), cleaned_data
def goal_input(request):
    if request.method == 'POST':
        form = GoalForm(request.POST)
        
        if form.is_valid():
            goal_name = form.clean_data['goal_name']
            target_amount= form.cleaned_data['target_amount']
            current_amount= form.cleaned_data['current_amount']
            deadline = form.cleaned_data['deadline']
            is_completed = form.cleaned_data['is_completed']
            user_id = form.cleaned_data['user_id']
            new_goal = Goal.objects.create(
                goal_name= goal_name,
                target_amount = target_amount,
                current_amount= current_amount,
                deadline = deadline,
                is_completed = is_completed,
                user_id = user_id)
            return redirect('goalist')
    else :
        form =  GoalForm()
    return render(request,'moodinput.html', {'form':form})