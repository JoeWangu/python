from django.urls import path, include
from rest_framework import routers

from rentalfinderapp.views.api import ImagesViewSet, RentalViewSet


router = routers.DefaultRouter()
router.register(r'images', ImagesViewSet, basename='images')
router.register(r'rentals', RentalViewSet, basename='rentals')


urlpatterns = [
    path('api/', include(router.urls)),
]
