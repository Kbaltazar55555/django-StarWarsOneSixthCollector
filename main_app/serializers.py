from rest_framework import serializers
from .models import SW
from .models import Custom
from .models import Vehicle

class SWSerializer(serializers.ModelSerializer):
    vehicles = VehicleSerializer(many=True, read_only=True)
    class Meta:
        model = SW
        fields = '__all__'


class CustomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Custom
        fields = '__all__'
        read_only_fields = ('sw',)

class VehicleSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Vehicle
        fields = '__all__'