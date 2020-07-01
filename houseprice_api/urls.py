from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register('houses', views.HouseView)
router.register('locations', views.LocationView)


urlpatterns = [
    path('', include(router.urls)), 
]
