from django import forms 
from .models import Goal, Mood

#errors - class Meta, structure of class GoalForm
class GoalForm(forms.ModelForm):
    class Meta:
        model = Goal
        fields = ['goal_name', 'target_amount', 'current_amount', 'deadline', 'isCompleted']
        
class MoodForm (forms.ModelForm):
    class Meta:
        model = Mood
        fields = ['mood_name', 'description', 'emoji']
        
        