from django.db import models

# Create your models here.
class Profile(models.Model):
    fullname = models.CharField(max_length=100)
    username =  models.CharField(max_length=100)
    email = models.CharField(max_length=100, unique=True)
    bio = models.CharField(max_length=100)

    