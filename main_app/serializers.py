from rest_framework import serializers
from .models import SW
from .models import Custom

class SWSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = SW
        fields = '__all__'


class CustomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Custom
        fields = '__all__'
        read_only_fields = ('sw',)