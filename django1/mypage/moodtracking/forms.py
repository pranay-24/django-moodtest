from django import forms 
from .models import Goal, Mood, Expense
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User

class CustomLoginForm(AuthenticationForm):
    pass
    
#errors - class Meta, structure of class GoalForm

class ExpenseForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = ['title', 'value', 'mood','expense_date']
        
class GoalForm(forms.ModelForm):
    class Meta:
        model = Goal
        fields = ['goal_name', 'target_amount', 'current_amount', 'deadline', 'isCompleted']
        
class MoodForm (forms.ModelForm):
    class Meta:
        model = Mood
        fields = ['mood_name', 'description', 'emoji']
        

class UserForm(forms.ModelForm):
    # password = forms.CharField(widget = forms.PasswordInput() )
    class Meta:
        model = User
        fields = ('username', 'email', 'password')
        