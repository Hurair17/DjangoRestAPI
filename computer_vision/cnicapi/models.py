from django.db import models

# Create your models here.

class Person(models.Model):
    id = models.IntegerField(unique=True,primary_key=True)
    cnic = models.IntegerField(unique=True)
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Vehicle(models.Model):
    cnic = models.OneToOneField(Person,on_delete=models.CASCADE) 
    created_at = models.DateTimeField(auto_now_add=True)
    car_model = models.CharField(max_length=100)
    car_name = models.CharField(max_length=100)
    
    id = models.IntegerField(unique=True,primary_key=True)
    
    class Meta:
        ordering = ['-created_at']
        
    def __str__(self):
        return self.car_model   



