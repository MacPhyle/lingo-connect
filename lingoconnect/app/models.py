from django.db import models

# Create your models here.

class User(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    username = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    languages_spoken = models.CharField(max_length=250)
    languages_to_learn = models.CharField(max_length=250)
    hobbies = models.CharField(max_length=250)

    
class Event(models.Model):
    title = models.CharField(max_length=100)
    location = models.CharField(max_length=50)
    category = models.CharField(max_length=50)
    date = models.DateField(max_length=50)
    time = models.TimeField(max_length=50)
    description = models.TextField(max_length=500)
    participants = models.ManyToManyField(User, related_name="events")