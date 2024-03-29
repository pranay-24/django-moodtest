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
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name = "expenses")
    title = models.CharField(max_length=100)
    value = models.DecimalField(max_digits=10, decimal_places=2)
    mood = models.ForeignKey(Mood, on_delete=models.CASCADE, null=True)
    expense_date = models.DateField(default=datetime.now)  # Defaulting to current date

#chose one to one mapping instead of inheriting directl from user model    
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # Add other fields as needed
    
    bio = models.TextField(blank=True)

    def __str__(self):
        return self.user.username

class Notifications(models.Model):
    message = models.CharField(max_length=200)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name = "notifications")
    timestamp = models.DateField(default=datetime.now)
        
# class Goal(models.Model):
#     title = models.CharField(max_length=200)
#     value = models.IntegerField() # can add validator lke IntegerField(validators = [MaxValueValidator(5), MinValueValidator(1)]) # and import MaxValuealidator from django.core.validators
#     isComplete = models.BooleanField(default=False)

class Goal(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name = "goals")
    goal_name = models.CharField(max_length=50)
    target_amount = models.DecimalField(max_digits=10, decimal_places=2)
    current_amount = models.DecimalField(max_digits=10, decimal_places=2)
    deadline = models.DateTimeField(default=datetime.now)  # Defaulting to current datetime
    isCompleted = models.BooleanField(default=False)

    def __str__(self):
        return self.goal_name
    
    def save(self, *args, **kwargs):
        is_new = self.pk is None
        super().save(*args, **kwargs)
        if is_new:
            Notifications.objects.create(
                user = self.user,
                message = f"goal created with goal name {self.goal_name}",
                timestamp = datetime.now()
            )
        
     

    