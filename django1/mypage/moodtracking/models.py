from django.db import models
from django.contrib.auth.models import User
from django import forms
from datetime import datetime
# Create your models here.

# class Mood(models.Model):
#     HAPPY = 'happy'
#     SAD = 'sad'
#     ANGRY = 'angry'
#     EXCITED = 'excited'
#     CALM = 'calm'

#     MOOD_CHOICES = [
#         (HAPPY, 'Happy'),
#         (SAD, 'Sad'),
#         (ANGRY, 'Angry'),
#         (EXCITED, 'Excited'),
#         (CALM, 'Calm'),
#     ]
    #mood choices enetered , but it is not working
    #can add default = "" , and can also add null=True
    # title = models.CharField(max_length = 30, choices=MOOD_CHOICES)
    # description = models.CharField(max_length = 200)
    # def __str__(self):
    #     return f"{self.title} ({self.description})"
    # overiding a built in method , can create slugs frm title using this method
    # def save(self, *args, **kwargs):
    #     #self.slug = slugify(self.title)
    #     self.title = self.title.capitalize()
    #     super().save(self,  *args, **kwargs)
        
class Mood(models.Model):
    mood_name = models.CharField(max_length = 50,  default = 'happy')
    description = models.CharField(max_length = 200, default = 'this is mood happy')
    emoji = models.CharField(max_length = 200, default  = '/static/images/1')
    
    def __str__(self):
        return f"{self.mood_name}"
    
class Expense(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    title = models.CharField(max_length=100)
    value = models.DecimalField(max_digits=10, decimal_places=2)
    mood = models.ForeignKey(Mood, on_delete=models.CASCADE, null=True, default=1)
    expense_date = models.DateField(default=datetime.now)  # Defaulting to current date
    
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # Add other fields as needed
    
    bio = models.TextField(blank=True)

    def __str__(self):
        return self.user.username
       
# class Goal(models.Model):
#     title = models.CharField(max_length=200)
#     value = models.IntegerField() # can add validator lke IntegerField(validators = [MaxValueValidator(5), MinValueValidator(1)]) # and import MaxValuealidator from django.core.validators
#     isComplete = models.BooleanField(default=False)

class Goal(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    goal_name = models.CharField(max_length=50, default = "limit 200")
    target_amount = models.DecimalField(max_digits=10, decimal_places=2, default=100.00)
    current_amount = models.DecimalField(max_digits=10, decimal_places=2, default=50.00)
    deadline = models.DateTimeField(default=datetime.now)  # Defaulting to current datetime
    isCompleted = models.BooleanField(default=False)

    def __str__(self):
        return self.goal_name
     
     
class Notifications(models.Model):
    message = models.CharField(max_length=200)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    timestamp = models.DateField(default=datetime.now)
    