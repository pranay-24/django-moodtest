from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect 
from django.urls import reverse
from django.template.loader import render_to_string
from .models import Mood, Goal, Expense
from .forms import MoodForm ,GoalForm, AuthenticationForm, UserForm
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required

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
# def mood_list (request):
       
#        moods = [ mood['mood_title'] for mood in moods_list]
#        moodPage = ""
 
#     #    for mood in moods_list:
#     #        moodPage += f'<li><a href={reverse("mood_url", args = [mood])}>{mood}</a></li>'
       
#     #    return HttpResponse(moodPage)
#        return render(request, "moodtracking/moodList.html",{"mood_list":moods}) 
   
# def find_goal(request,goal):
#     return HttpResponse(f"this is the goal page for:  {goal}")

# def mood_bynumber1(request,mood_number):
#     mood_list = list(moods_dict.keys())
#     mood_redirect= mood_list[mood_number]
    
#     return HttpResponseRedirect("/moods"+ mood_redirect)

## -------------
# goals

##------
# filtering Syntax
# next(  post for post in posts if post['slug']== slug )


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
# def find_mood(request, mood_id):
#     mood = Mood.objects.filter(id= mood_id)
#     return render(request, "", {"mood":mood})

# def find_moods(request):
#     moods = Mood.objects.all()
#     return render(request,"", {"moods":moods})

# solved errors- it should be appname/templatename

def expense_list(request):
    expenses = Expense.objects.all()
    return render(request, 'moodtracking/expense_list.html', {'expenses': expenses})


def mood_list (request):
    moods = Mood.objects.all()
    return render(request, 'moodtracking/mood_list.html', {'moods': moods})


def goal_list (request):
    goals = Goal.objects.all()
    return render(request, 'moodtracking/goal_list.html', {'goals': goals})



# View expense

def expense_detail(request, expense_id):
    expense = get_object_or_404(Expense, id=expense_id)
    return render(request, 'moodtracking/expense_detail.html', {'expense': expense})

def mood_detail(request,  mood_id):
    mood = get_object_or_404(Expense, id=mood_id)
    return render(request, 'moodtracking/mood_detail.html', {'mood': mood})

def goal_detail(request, goal_id):
    goal = get_object_or_404(Expense, id=goal_id)
    return render(request, 'moodtracking/goal_detail.html', {'goal': goal})



#index , login register views

def index(request):
    return render(request, 'moodtracking/index.html')


def register(request):
    registered = False
    
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        
        if user_form.is_valid():
            user = user_form.save()
            user.save()
            registered = True
        else:
            print(user_form.errors)
    else:
        user_form = UserForm()
    
    return render(request, 'moodtracking/registration.html', {'user_form': user_form, 'registered': registered})

def custom_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password= password)
            if user is not None:
                login(request,user)
                return redirect('expense-list')
            else:
                form.add_error(None, 'Invalid username or password')
    
    else:
        form = AuthenticationForm()
        
    return render(request, 'moodtracking/login.html', {'form': form})

    
def custom_logout(request):
    logout(request)
    return redirect('login')
    
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
    return render(request,'moodtracking/moodinput.html', {'form':form})