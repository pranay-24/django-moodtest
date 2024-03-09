# from django.db import models

# class Product(models.Model):
#     id = models.CharField(max_length =100)
#     name = models.CharField(max_length = 100)
#     price = models.DecimalField(max_digits = 10, decimal_places =2)
#     category = models.CharField(max_length = 100)


from django.db import models

class Mood(models.Model):
    title = models.CharField(max_lengtg = 100)
    image_url = models.URLField()
    
    
class transaction(models.Model):
    title = models.CharField(max_length  = 100)
    value = models.DecimalField(max_digits = 10 , decimal_places = 2)
    mood = models.ForeignKey(Mood, on_delete = models.CASCADE)
