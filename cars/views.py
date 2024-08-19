from django.shortcuts import render
from rest_framework import generics
from .models import Car
from .serializers import CarSerializer
from rest_framework.permissions import IsAuthenticated
from .permisssions import IsOwnerOrReadOnly
# Create your views here.

class CarList(generics.ListAPIView):
  
  queryset = Car.objects.all()
  serializer_class = CarSerializer
  
# cars/views.py

class CarListView(generics.ListCreateAPIView): # ListAPIView, returen list without ability to add new record
    
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    
class CarDetailsView(generics.RetrieveUpdateDestroyAPIView): # RetrieveAPIView, return details of one record without ability to update the details
  permission_classes = [IsAuthenticated]
  permission_classes = [IsOwnerOrReadOnly]
  queryset = Car.objects.all()
  serializer_class = CarSerializer



  
  

