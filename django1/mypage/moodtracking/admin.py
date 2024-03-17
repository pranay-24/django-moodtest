from django.contrib import admin
from . import models
# Register your models here.



class MoodAdmin(admin.ModelAdmin):
    list_display = ('mood_name', 'description', 'emoji',) 
    list_filter = ('mood_name',)
    
class GoalAdmin(admin.ModelAdmin):
    list_display = ('goal_name', 'target_amount', 'current_amount', 'deadline', 'isCompleted',)
    list_filter = ('goal_name', 'isCompleted',)
    
admin.site.register (models.Expense)
admin.site.register(models.Mood, MoodAdmin)
admin.site.register(models.Goal, GoalAdmin) 