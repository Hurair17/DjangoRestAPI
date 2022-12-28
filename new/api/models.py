from django.db import models

# Create your models here.

class Person(models.Model):
    cnic = models.IntegerField(unique=True,primary_key=True)
    name = models.CharField(max_length=100)
    def __int__(self):
        return self.cnic

class Vehicle(models.Model):
    cnic = models.ForeignKey(Person,on_delete = models.CASCADE) 
    created_at = models.DateTimeField(auto_now_add=True)
    car_model = models.CharField(max_length=100)
    car_name = models.CharField(max_length=100)
    number_plate = models.CharField(max_length=10)
    
    
    class Meta:
        ordering = ['-created_at']
        
    def __str__(self):
        return self.car_model   


class ImageUpload(models.Model):
    cnic = models.CharField(max_length=20)
    image = models.ImageField(max_length=None)
    car_number = models.CharField(max_length=100)


