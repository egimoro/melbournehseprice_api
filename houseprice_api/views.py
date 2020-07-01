from .models import House, Location
from rest_framework import viewsets
from .serializers import HouseSerializer, LocationSerializer
from rest_framework.exceptions import APIException
from django.db import IntegrityError

# Create your views here.

class HouseView(viewsets.ModelViewSet):
    queryset = House.objects.all().order_by('-datesold')
    serializer_class = HouseSerializer
    

class LocationView(viewsets.ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer
    
    
        

