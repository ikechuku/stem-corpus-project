from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.


class Info(models.Model):
    user = models.OneToOneField(User, related_name='Info',on_delete=models.CASCADE, null=True, blank=True)
    fullname = models.CharField(max_length=100, blank = False)
    username =  models.CharField(max_length=100, blank = False)
    email = models.EmailField(max_length=100, unique=True)
    bio = models.TextField(max_length=100, blank = False)

class Article(models.Model):
    user = models.OneToOneField(User, related_name='Article',on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=200, blank=False)
    article = models.TextField(max_length=500, blank=False)
    cloudinary_id = models.CharField(max_length=200,blank=False , default = '')
    image_url = models.URLField(max_length=500, blank=False, default='')

class Portfolio(models.Model):
     user = models.OneToOneField(User, related_name='Portfolio', on_delete=models.CASCADE, blank=True)
     cloudinary_id = models.CharField(max_length=200,blank=False)
     image_url = models.URLField(max_length=500, blank=False)
     name = models.CharField(max_length=200, blank=False)
     text = models.TextField(max_length=500, blank=False)

@receiver(post_save, sender=User)
def create_user_Info(sender, instance, created, **kwargs):
    if created:
        Info.objects.create(user=instance)
def create_user_Article(sender, instance, created, **kwargs):
    if created:
        Article.objects.create(user=instance)
def create_user_Portfolio(sender, instance, created, **kwargs):
    if created:
        Portfolio.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_Info(sender, instance, **kwargs):
    instance.Info.save()
def save_user_Article(sender, instance, **kwargs):
    instance.Article.save()
def save_user_Portfolio(sender, instance, **kwargs):
    instance.Portfolio.save()