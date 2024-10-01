from django.conf import settings
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
    
class Event(models.Model):
    title = models.CharField(max_length=200)
    location = models.CharField(max_length=50)
    category = models.CharField(max_length=50)
    date = models.DateField()
    time = models.TimeField()
    description = models.TextField(max_length=500)
    participants = models.ManyToManyField(User, related_name="events")
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="owned_events", default=1)
    
    def __str__(self):
        return self.title