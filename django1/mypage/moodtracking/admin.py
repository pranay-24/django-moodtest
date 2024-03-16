from django.contrib import admin
from . import models
# Register your models here.

class ExpenseAdmin(admin.ModelAdmin):
    list_display = ('expense_date', 'title', 'value', 'mood' )
    list_filter = ('mood',)

class MoodAdmin(admin.ModelAdmin):
    list_display = ('title',  'description') 
    
admin.site.register (models.Expense, ExpenseAdmin)
admin.site.register(models.Mood, MoodAdmin)