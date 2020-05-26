from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# This represents the grave of a player's character
class Gravemarker(models.Model):
    name = models.CharField(max_length = 50)
    race = models.CharField(max_length = 50)
    charclass = models.CharField(max_length = 50)
    liferange = models.CharField(max_length = 50)
    enscription = models.CharField(max_length = 150)
    date_created = models.DateTimeField(default=timezone.now)
    createdby = models.ForeignKey(User, models.CASCADE)

    def __str__(self):
        return self.name