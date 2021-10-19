from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.urls import reverse


class Dog(models.Model):
    name = models.CharField(max_length=100)
    weight = models.DecimalField(max_digits=4, decimal_places=2)
    dob = models.DateField()
    image = models.ImageField(null=True, blank=True, upload_to="images/")
    description = models.TextField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.name + ' : ' + str(self.owner)
    def get_absolute_url(self):
        return reverse('home')

class Activity(models.Model):
    name = models.CharField(max_length=200)
    date = models.DateField()
    description = models.TextField()
    location = models.TextField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    def get_absolute_url(self):
        return reverse('home')