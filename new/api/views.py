from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework import status
from .serializers import ImageUploadSerializer
from rest_framework.response import Response
# Create your views here.
from .image_classify import predict_classify

from django.shortcuts import render
from .models import Vehicle,Person,ImageUpload
from .serializers import PersonSerializer,CarsSerializer,ImageUploadSerializer,ImageSerializer,CNICSerializer,CNICNumberPlateSerializer
from django.shortcuts import get_object_or_404
from django.http import JsonResponse,HttpResponseBadRequest
from PIL import Image
import numpy as np

# Create your views here.

# def person_detail(request,cnic):
#     stu = Person.objects.get(cnic = cnic)
#     serilizer = PersonSerializer(stu)
#     return JsonResponse(serilizer.data)
# class PersonDetail(APIView):
#     def get(self, request, format=None):
#         serializer = CNICSerializer(data=request.data)
#         if serializer.is_valid():
#             cnic = serializer.validated_data['cnic']
#             # stu = Person.objects.get(cnic = cnic)
#             # serializer = PersonSerializer(stu)
#             stu = Person.objects.get(cnic = cnic)
#             serilizer = PersonSerializer(stu)
#             return JsonResponse(serilizer.data)
#             # return JsonResponse(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    
    
# class ImageUploadViewSet(viewsets.ModelViewSet):
#     queryset = ImageUpload.objects.all()
#     serializer_class = ImageUploadSerializer

# class FileView(APIView):
#   parser_classes = (MultiPartParser, FormParser)
#   def post(self, request, *args, **kwargs):
#     file_serializer = ImageUploadSerializer(data=request.data)
#     if file_serializer.is_valid():
#         print('Image as print',file_serializer.type)
#         file_serializer.save()
#         return Response(file_serializer.data, status=status.HTTP_201_CREATED)
#     else:
#       return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# def vehicle_detail(request):
#     serializer = CNICSerializer(data=request.data)
#     if serializer.is_valid():
#         cnic = serializer.validate['cnic']
#         stu = Vehicle.objects.filter(cnic_id = cnic)
#         serializer = CarsSerializer(stu,many=True)
#         return JsonResponse(serializer.data,safe=False)
#     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class VehicleDetail(APIView):
    def post(self, request, format=None):
        serializer = CNICNumberPlateSerializer(data=request.data)
        if serializer.is_valid():
            cnic = serializer.validated_data['cnic']
            cnic = cnic.replace('-', '')
            stu = Vehicle.objects.filter(cnic_id = cnic)
            serializer = CarsSerializer(stu,many=True)
            return JsonResponse(serializer.data,safe=False)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
# class SelectedVehicleDetail(APIView):
#     def post(self, request,*args, **kwargs,):
#         serializer = CNICSerializer(data=request.data)
#         if serializer.is_valid():
#             cnic = serializer.validated_data['cnic']
#             number_plate = serializer.validated_data['number_plate']
#             cnic = cnic.replace('-', '')
#             stu = Vehicle.objects.filter(cnic_id = cnic)
#             serializer = CarsSerializer(stu,many=True)
#             stu = Vehicle.objects.filter(number_plate = number_plate)
#             serializer = CarsSerializer(stu,many=True)
            
#             return JsonResponse(serializer.data,safe=False)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ImageView(APIView):
    parser_classes = (MultiPartParser, FormParser)
    def post(self, request, format=None):
        # serializer = ImageSerializer(data=request.data)
        serializer = ImageUploadSerializer(data=request.data)
        if serializer.is_valid():
            # Save the image and classify its contents
            image = serializer.validated_data['image']
            #Model for demage car prediction
            # classification = predict_classify(image)
            print(image.name)
            # print(classification)
            classification = serializer.validated_data['cnic']
            # classification = image.name
            # if classification== "demaged.JPEG":
            #     serializer.save()
            #     classification = 'Car is damage'
            # else:
            #     classification = 'Cars is not damage'
            if classification== "1":
                serializer.save()
                classification = 'Car is damage'
            else:
                classification = 'Cars is not damage'
            return Response({'classification': classification})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
    


    


