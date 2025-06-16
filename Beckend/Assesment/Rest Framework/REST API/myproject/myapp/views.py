from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
import requests
from rest_framework import generics
from .models import Doctor
from .serializers import DoctorSerializer 

@api_view(['GET'])
def get_random_joke(request):
    url = "https://official-joke-api.appspot.com/jokes/random"
    response = requests.get(url)
    
    if response.status_code == 200:
        joke_data = response.json()
        return Response({"setup": joke_data["setup"], "punchline": joke_data["punchline"]})
    else:
        return Response({"error": "Failed to fetch joke"}, status=response.status_code)

class DoctorListCreateView(generics.ListCreateAPIView):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer

class DoctorRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):  # ✅ Fixed typo
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer
