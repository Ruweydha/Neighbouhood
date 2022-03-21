from distutils.command.upload import upload
from django.db import models
from django.contrib.auth.models import User
from django.forms import CharField

# Create your models here.
class Neighbourhood(models.Model):
    name = models.CharField(max_length=30)
    location = models.CharField(max_length=30)
    Admin  = models.ForeignKey(User, on_delete=models.CASCADE)

    def create_neigbourhood(self):
        self.save()

    def delete_neighbourhood(self):
        self.delete()

    @classmethod
    def update_neighbourhood(cls, id):
        cls.objects.filter(id=id).update()

    @classmethod
    def find_neighbourhood(cls, neighborhood_id):
        return cls.objects.filter(id=neighborhood_id)
    

class Police(models.Model):
    name = models.CharField(max_length=30)
    neighbourhood = models.ForeignKey(Neighbourhood, on_delete=models.CASCADE)
    contact = models.CharField(max_length=10)
    email = models.EmailField()
    alternative_contact = models.CharField(max_length=10)

    def __str__(self):
        return self.name

class HealthDepartment(models.Model):
    name = models.CharField(max_length=30)    
    neighbourhood = models.ForeignKey(Neighbourhood, on_delete=models.CASCADE)
    contact = models.CharField(max_length=10)
    email = models.EmailField()
    alternative_contact = models.CharField(max_length=10) 

    def __str__(self):
        return self.name

class Occupants(models.Model):
    name = models.CharField(max_length=30, default='Ru')
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    neighbourhood = models.ForeignKey(Neighbourhood, on_delete=models.CASCADE)
    id_number = models.CharField(max_length=8)
    email = models.EmailField()
    profile_pic = models.ImageField(upload_to = 'profile')
    location = models.CharField(max_length=30)
    about_me = models.CharField(max_length=150)

    def __str__(self):
        return self.name

class Businesses(models.Model):
    name = models.CharField(max_length=30, default='max')
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    neighbourhood = models.ForeignKey(Neighbourhood, on_delete=models.CASCADE)
    email = models.EmailField()

    def __str__(self):
        return self.name

    def create_business(self):
        self.save()

    def delete_business(self):
        self.delete()

    @classmethod
    def update_business(cls, id):
        cls.objects.filter(id=id).update()

    @classmethod
    def find_business(cls, neighborhood_id):
        return cls.objects.filter(id=neighborhood_id)    

    @classmethod
    def search_by_name(cls,search_term):
        business = cls.objects.filter(name__icontains=search_term)
        return business   
    
class Posts(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    neighbourhood = models.ForeignKey(Neighbourhood, on_delete=models.CASCADE)
    post = models.CharField(max_length=300)
