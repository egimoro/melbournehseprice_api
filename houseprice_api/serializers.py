from .models import Location, House
from rest_framework import serializers



class HouseSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = House
        fields = ('rooms', 'hsetype', 'price', 'method', 'datesold',
                  'seller')



class LocationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Location
        fields = ('suburb', 'address', 'postcode', 'regionname',
                    'propertycount', 'distance', 'house')
    
    
    
