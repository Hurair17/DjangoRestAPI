
from django.contrib import admin
from django.urls import path
from cnicapi import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('person/<int:cnic>',views.person_detail),
    path('vehicle/<int:cnic_id>',views.vehicle_detail),
    path('vehicle/',views.all_vehicle),
    
    
    
]
