from rest_framework import serializers
from .models import Vehicle,Person,ImageUpload

class PersonSerializer(serializers.Serializer):
    class Meta:
        model = Person
        fields = "__all__"
    

class CarsSerializer(serializers.ModelSerializer):
    # cnic_id = serializers.PrimaryKeyRelatedField(queryset=Person.objects.all())
    # cnic_id = queryset=Person.objects.all()
    class Meta:
        model = Vehicle
        fields = "__all__"
   
    

class ImageUploadSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = ImageUpload
        fields= "__all__"
   
   
#For taking data in the request as json
class ImageSerializer(serializers.Serializer):
    image = serializers.ImageField()
    
class CNICSerializer(serializers.Serializer):
    cnic = serializers.CharField()
    number_plate = serializers.CharField()
    
class CNICNumberPlateSerializer(serializers.Serializer):
    cnic = serializers.CharField()
   