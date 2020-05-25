from django.db import models

# This represents a real person who owns characters
class Player(models.Model):
    username = 

# This represents the grave of a player's character
class Grave(models.Model):
    name = models.CharField(max_length = 50)
    race = models.CharField(max_length = 50)
    charclass = models.CharField(max_length = 50)
    liferange = models.CharField(max_length = 50)
    enscription = models.CharField(max_length = 150)
    #playedby = models.
