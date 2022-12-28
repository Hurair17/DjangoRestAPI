from django.contrib import admin

from .models import Vehicle,Person,ImageUpload
# Register your models here.
@admin.register(Person)
class CarsAdmin(admin.ModelAdmin):
    list_display = ['cnic','name']
    
@admin.register(Vehicle)
class CarsAdmin(admin.ModelAdmin):
    list_display = ['cnic','car_model','car_name','number_plate']
    
@admin.register(ImageUpload)
class ImageUpload(admin.ModelAdmin):
    list_display = ['cnic','image','car_number']
