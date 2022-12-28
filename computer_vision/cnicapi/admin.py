from django.contrib import admin

from .models import Vehicle,Person
# Register your models here.
@admin.register(Person)
class CarsAdmin(admin.ModelAdmin):
    list_display = ['cnic','name']
    
@admin.register(Vehicle)
class CarsAdmin(admin.ModelAdmin):
    list_display = ['cnic','car_model','car_name',]
