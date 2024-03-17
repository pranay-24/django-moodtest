from django.db import models
from django.contrib.auth.models import User
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
    mood_id  = models.CharField(max_length = 10, primary_key = True)
    mood_name = models.CharField(max_length = 50)
    description = models.CharField(max_length = 200)
    emoji = models.ImageField(upload_to='images/')
    
    def __str__(self):
        return f"{self.mood_name}"
    
class Expense(models.Model):
    expense_id = models.CharField(max_length = 10, primary_key = True)  
    user = models.ForeignKey(User, on_delete = models.CASCADE )
    title = models.CharField(max_length = 100)
    value = models.IntegerField()
    mood = models.ForeignKey(Mood, on_delete = models.CASCADE)
    expense_date = models.DateField()

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
     goal_id  = models.CharField(max_length = 10, primary_key = True)   
     user_id = models.ForeignKey('', on_delete = models.CASCADE )
     goal_name = models.CharField(max_length = 50)
     target_amount = models.DecimalField(deciaml_places = 2)
     current_amount = models.DecimalField(deciaml_places = 2)
     deadline = models.DateTimeField()
     isCompleted = models.BooleanField(default= False)
     
     def __str__(self):
            return self.goal_name
     
class Notifications(models.Model): 
    notification_id  = models.CharField(max_length = 10 , primary_key = True)
    message = models.CharField(max_length=200)
    user_id = models.ForeignKey('', on_delete = models.CASCADE )
    timestamp = models.DateField()
    