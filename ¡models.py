from django.conf import settings
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# class User(models.Model):
#     first_name = models.CharField(max_length=100)
#     last_name = models.CharField(max_length=100)
#     username = models.CharField(max_length=50)
#     email = models.EmailField(unique=True)
#     languages_spoken = models.CharField(max_length=250)
#     languages_to_learn = models.CharField(max_length=250)
#     hobbies = models.CharField(max_length=250)
#     profile_picture = models.ImageField(upload_to='profile_pictures/', default='static/images/default_profile_picture.png')
    
class Event(models.Model):
    title = models.CharField(max_length=100)
    location = models.CharField(max_length=50)
    category = models.CharField(max_length=50)
    date = models.DateField()
    time = models.TimeField()
    description = models.TextField(max_length=500)
    participants = models.ManyToManyField(User, related_name="events")
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="owned_events", default=1)