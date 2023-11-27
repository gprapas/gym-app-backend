from rest_framework import serializers
from .models import GymFile
class GymFileSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = GymFile
        fields = '__all__'