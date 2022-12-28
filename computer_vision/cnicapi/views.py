from django.shortcuts import render
from .models import Vehicle,Person
from .serializers import PersonSerializer,CarsSerializer
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
# Create your views here.

def person_detail(request,cnic):
    stu = Person.objects.get(cnic = cnic)
    serilizer = PersonSerializer(stu)
    return JsonResponse(serilizer.data)

def all_vehicle(request):
    stu = Vehicle.objects.all()
    serializer = CarsSerializer(stu, many=True)
    return JsonResponse(serializer.data,safe=False)


def vehicle_detail(request,cnic_id):
    stu = Vehicle.objects.get(cnic_id = cnic_id)
    serializer = CarsSerializer(stu)
    return JsonResponse(serializer.data,safe=False)
    
    
      



