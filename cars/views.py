from django.shortcuts import render
from rest_framework import generics
from .models import Car
from .serializers import CarSerializer

# Create your views here.

class CarList(generics.ListAPIView):
  
  queryset = Car.objects.all()
  serializer_class = CarSerializer
  
# cars/views.py

class CarListView(generics.ListCreateAPIView): # ListAPIView, returen list without ability to add new record
    
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    
class CarDetailsView(generics.RetrieveUpdateDestroyAPIView): # RetrieveAPIView, return details of one record without ability to update the details

  queryset = Car.objects.all()
  serializer_class = CarSerializer



  
  

