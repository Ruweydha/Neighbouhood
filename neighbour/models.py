import email
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Neighbourhood(models.Model):
    name = models.CharField(max_length=30)
    location = models.CharField(max_length=30)
    Admin  = models.ForeignKey(User, on_delete=models.CASCADE)

class Police(models.Model):
    neighbourhood = models.ForeignKey(Neighbourhood, on_delete=models.CASCADE)
    contact = models.CharField(max_length=10)
    email = models.EmailField()
    alternative_contact = models.CharField(max_length=10)

class HealthDepartment(models.Model):
    neighbourhood = models.ForeignKey(Neighbourhood, on_delete=models.CASCADE)
    contact = models.CharField(max_length=10)
    email = models.EmailField()
    alternative_contact = models.CharField(max_length=10)        

