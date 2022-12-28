from rest_framework import serializers
from .models import Vehicle,Person

class PersonSerializer(serializers.Serializer):
    class Meta:
        model = Person
        fields = (
            'cnic',
            'name'
        )
    

class CarsSerializer(serializers.ModelSerializer):
    cnic = serializers.PrimaryKeyRelatedField(queryset=Person.objects.all())
    class Meta:
        model = Vehicle
        fields = ('cnic', 
                  'car_model',
                  'car_name'
                  'id'
                  )
   
    



   
   
   