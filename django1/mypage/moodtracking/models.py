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
    
    title = models.CharField(max_length = 30, choices=MOOD_CHOICES)
    description = models.CharField(max_length = 200)
    def __str__(self):
        return f"{self.title} ({self.description})"

class Transaction(models.Model):
    title = models.CharField(max_length = 100)
    value = models.IntegerField()
    mood = models.ForeignKey(Mood, on_delete = models.CASCADE)