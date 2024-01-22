from rest_framework import viewsets
# from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import AllowAny
# from rest_framework.permissions import IsAuthenticated
from rentalfinderapp.models import Images, Rental
from rentalfinderapp.serializers import ImagesSerializer, RentalSerializer


class ImagesViewSet(viewsets.ModelViewSet):
    queryset = Images.objects.all().order_by('id')
    serializer_class = ImagesSerializer


class RentalViewSet(viewsets.ModelViewSet):
    queryset = Rental.objects.all().order_by('id')
    serializer_class = RentalSerializer
    # permission_classes = [AllowAny]
    # authentication_classes = [TokenAuthentication]
    # permission_classes = [IsAuthenticated]
