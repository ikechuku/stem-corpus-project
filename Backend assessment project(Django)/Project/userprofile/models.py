from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.


class Details(models.Model):
    user = models.OneToOneField(User, related_name='Details',on_delete=models.CASCADE)
    fullname = models.CharField(max_length=100, blank = False)
    username =  models.CharField(max_length=100, blank = False)
    email = models.EmailField(max_length=100, unique=True)
    bio = models.TextField(max_length=100, blank = False)

class Bio(models.Model):
    user = models.OneToOneField(User, related_name='Bio',on_delete=models.CASCADE)
    title = models.CharField(max_length=100, blank=False)
    article = models.TextField(max_length=100, blank=False)

    
@receiver(post_save, sender=User)
def create_user_Details(sender, instance, created, **kwargs):
    if created:
        Details.objects.create(user=instance)
def create_user_Bio(sender, instance, created, **kwargs):
    if created:
        Bio.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_Details(sender, instance, **kwargs):
    instance.Details.save()
def save_user_Bio(sender, instance, **kwargs):
    instance.Bio.save()