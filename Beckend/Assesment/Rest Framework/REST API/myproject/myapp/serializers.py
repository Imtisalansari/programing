from rest_framework import serializers
from .models import Doctor  # Make sure this import is correct

class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = '__all__'