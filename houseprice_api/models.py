from django.db import models

class House(models.Model):
    
    

    rooms = models.IntegerField(default=0)
    hsetype = models.CharField(max_length=2)
    price = models.FloatField(default=0)
    method = models.CharField(max_length=3)
    datesold = models.DateField()
    seller = models.CharField(max_length=250)
    
    def __str__(self):
        return self.seller
    
class Location(models.Model):
    
   

    suburb = models.CharField(max_length=250)
    address = models.CharField(max_length=250)
    postcode = models.CharField(max_length=4)
    propertycount = models.IntegerField(default=0)
    regionname = models.CharField(max_length=250)
    distance = models.FloatField(default=0)
    house = models.ForeignKey(House, on_delete=models.CASCADE)

    def __str__(self):
        return self.suburb
