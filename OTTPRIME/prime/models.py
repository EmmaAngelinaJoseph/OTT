from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Customer(models.Model):
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(unique=True)
    mobile = models.CharField(max_length=15, blank=True, null=True)
    dob = models.DateField(blank=True, null=True)
    password=models.CharField(max_length=6, unique=True)

    def __str__(self):
        return self.username

class UserProfile(models.Model):
    user=models.ForeignKey(Customer,on_delete=models.CASCADE,null=True)
    subscription_plan = models.CharField(max_length=100, blank=True, null=True)
    expiry_date = models.DateField(blank=True, null=True)
    action = models.CharField(max_length=150, blank=True)

    def __str__(self):
        return self.subscription_plan
class movies(models.Model):
        title = models.CharField(max_length=150, unique=True)
        description = models.TextField(blank=True, null=True)
        genres = models.CharField(max_length=100, blank=True, null=True)
        director = models.CharField(max_length=100, blank=True, null=True)
        main_actor = models.CharField(max_length=100, blank=True, null=True)
        duration = models.IntegerField(blank=True, null=True)  # Duration in minutes
        image = models.ImageField(upload_to='movie/images/', blank=True, null=True)
        video = models.FileField(upload_to='movie/videos/', blank=True, null=True)
        disabled = models.BooleanField(default=False)

        def __str__(self):
            return self.title