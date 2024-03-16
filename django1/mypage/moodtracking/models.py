from django.db import models

# Create your models here.

class Mood(models.Model):
    HAPPY = 'happy'
    SAD = 'sad'
    ANGRY = 'angry'
    EXCITED = 'excited'
    CALM = 'calm'

    MOOD_CHOICES = [
        (HAPPY, 'Happy'),
        (SAD, 'Sad'),
        (ANGRY, 'Angry'),
        (EXCITED, 'Excited'),
        (CALM, 'Calm'),
    ]
    #mood choices enetered , but it is not working
    #can add default = "" , and can also add null=True
    title = models.CharField(max_length = 30, choices=MOOD_CHOICES)
    description = models.CharField(max_length = 200)
    def __str__(self):
        return f"{self.title} ({self.description})"
    # overiding a built in method , can create slugs frm title using this method
    # def save(self, *args, **kwargs):
    #     #self.slug = slugify(self.title)
    #     self.title = self.title.capitalize()
    #     super().save(self,  *args, **kwargs)
        

class Expense(models.Model):
    title = models.CharField(max_length = 100)
    value = models.IntegerField()
    mood = models.ForeignKey(Mood, on_delete = models.CASCADE)
    expense_date = models.DateField()
    
class Goal(models.Model):
    title = models.CharField(max_length=200)
    value = models.IntegerField() # can add validator lke IntegerField(validators = [MaxValueValidator(5), MinValueValidator(1)]) # and import MaxValuealidator from django.core.validators
    isComplete = models.BooleanField(default=False)
    
class Notifications(models.Model): 
    title = models.CharField(max_length=200)
    date = models.DateField()
    