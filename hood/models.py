from django.db import models
from pyuploadcare.dj.models import ImageField
from django.contrib.auth.models import User
# from .choices import choices

class Neighbourhood(models.Model):
    name = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    occupants = models.PositiveIntegerField(default=0)

    def save_neighbourhood(self):
        self.save()

    def delete_neighbourhood(self):
        self.delete()

    def __str__(self):
        return self.name

class Profile(models.Model):
    avatar = ImageField(blank = True, manual_crop='')
    bio = models.TextField()
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    neighbourhood = models.ForeignKey(Neighbourhood, on_delete=models.CASCADE)

    def save_profile(self):
        self.save()

    def __str__(self):
        return self.neighbourhood.name


class Business(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    neighbourhood = models.ForeignKey(Neighbourhood, on_delete=models.CASCADE)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)

    def save_business(self):
        self.save()

    def __str__(self):
        return self.name

