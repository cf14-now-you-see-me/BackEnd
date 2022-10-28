from rest_framework import serializers

from .models import *

class PlaceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Place
        fields = ('id', 'name', 'description', 'google_id', 'location', 'url')

class AmenitySerializer(serializers.HyperlinkedModelSerializer):
    place_name = serializers.SerializerMethodField()
    class Meta:
        model = Amenity
        fields = ('id', 'name', 'info', 'google_id', 'near', 'place_name', 'url')
    def get_place_name(self, obj):
        if obj.near is None:
            return None
        else:
            return obj.near.name