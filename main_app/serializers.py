from rest_framework import serializers
from .models import SW
from .models import Custom
from .models import Vehicle
from django.contrib.auth.models import User # add this line to list of imports


class VehicleSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Vehicle
        fields = '__all__'

class SWSerializer(serializers.ModelSerializer):
    vehicles = VehicleSerializer(many=True, read_only=True)
    user = serializers.PrimaryKeyRelatedField(read_only=True)  # Make the user field read-only

    class Meta:
        model = SW
        fields = '__all__'


class CustomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Custom
        fields = '__all__'
        read_only_fields = ('sw',)

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)  # Add a password field, make it write-only

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')
    
    def create(self, validated_data):
      user = User.objects.create_user(
          username=validated_data['username'],
          email=validated_data['email'],
          password=validated_data['password']  # Ensures the password is hashed correctly
      )
      
      return user
