from rest_framework import serializers
from .models import SW

class SWSerializer(serializers.ModelSerializer):
    class Meta:
        model = SW
        fields = '__all__'