from django.contrib import admin
from . import models
# Register your models here.


    
class ExpenseAdmin(admin.ModelAdmin):
    list_display = ('title', 'value', 'mood','expense_date', 'user') 
    list_filter = ('mood',)

class MoodAdmin(admin.ModelAdmin):
    list_display = ('mood_name', 'description', 'emoji',) 
    list_filter = ('mood_name',)
    
class GoalAdmin(admin.ModelAdmin):
    list_display = ('goal_name', 'target_amount', 'current_amount', 'deadline', 'isCompleted',)
    list_filter = ('goal_name', 'isCompleted',)
    
admin.site.register (models.Expense, ExpenseAdmin)
admin.site.register(models.Mood, MoodAdmin)
admin.site.register(models.Goal, GoalAdmin) 

#registering the userProfile to admin.site
admin.site.register(models.UserProfile)