from django.db import models

# Create your models here.
class Tweets(models.Model):    
    id = models.CharField(max_length=100, unique=True, primary_key = True)
    tweet_id = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    text = models.CharField(max_length=1000)    
    user = models.CharField(max_length=1000)
    domain = models.CharField(max_length=1000)
    profile_image = models.CharField(max_length=100)
