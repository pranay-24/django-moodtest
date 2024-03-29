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
@login_required
def expense_list(request):
    current_user = request.user
    expenses = current_user.expenses.all()
    return render(request, 'moodtracking/expense_list.html', {'expenses': expenses})


def mood_list (request):
    moods = Mood.objects.all()
    return render(request, 'moodtracking/mood_list.html', {'moods': moods})

#dont want all goals, want all goads for a  user, that user will also come from request
@login_required
def goal_list (request):
    current_user = request.user
    # print(current_user)
    goals = current_user.goals.all()
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

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username= username, password = password)
        if user : 
            login(request, user)
            return HttpResponseRedirect(reverse('expense-list'))
        else:
            
            return HttpResponse('Invalid details ')
    else:
        return render(request, 'moodtracking/login.html',{})

@login_required   
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('login'))

@login_required
def special(request):
    return HttpResponse("You are logged in")  

#creating view function to input the goal
#errors solved - is_valid(), request.method == POST, form(request.POST), cleaned_data
#removed user_id, userwill ocme from requrest.user if authenticated
@login_required
def goal_input(request):
    if request.method == 'POST':
        goal_form = GoalForm(request.POST)
        
        if goal_form.is_valid():
            goal_name = goal_form.cleaned_data['goal_name']
            target_amount= goal_form.cleaned_data['target_amount']
            current_amount= goal_form.cleaned_data['current_amount']
            deadline = goal_form.cleaned_data['deadline']
            isCompleted = goal_form.cleaned_data['isCompleted']
            # user_id = goal_form.cleaned_data['user_id']
            new_goal = Goal.objects.create(
                goal_name= goal_name,
                target_amount = target_amount,
                current_amount= current_amount,
                deadline = deadline,
                isCompleted = isCompleted,
                # user_id = user_id
                user = request.user
                )
            new_goal.save()
            return redirect('goal-list')
    else :
        goal_form =  GoalForm()
    return render(request,'moodtracking/goal_create.html', {'goal_form':goal_form})


 