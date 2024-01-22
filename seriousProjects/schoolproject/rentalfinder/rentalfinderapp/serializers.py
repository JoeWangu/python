from rest_framework import serializers
from rentalfinderapp.models import Rental, Images


class ImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Images
        fields = '__all__'


class RentalSerializer(serializers.HyperlinkedModelSerializer):
    image = serializers.PrimaryKeyRelatedField(queryset=Images.objects.all())
    image_detail = ImagesSerializer(source='image', read_only=True)

    class Meta:
        model = Rental
        fields = [
            # 'user',
            'name', 'image',
            'price', 'description', 'type',
            'location', 'available', 'rating',
            'total_units', 'date_posted', 'date_modified',
            'image_detail'
        ]
