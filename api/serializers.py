from .models import *
from rest_framework import serializers
from rest_framework.reverse import reverse

class UserSerializer(serializers.HyperlinkedModelSerializer):
    password = serializers.CharField(write_only=True)
    def create(self, valdata):
        user = User.objects.create_user(
            username=valdata['username'],
            password=valdata['password'],
            email=valdata['email'],
            profile_pic=valdata['profile_pic'],
            nat_id=valdata['nat_id'],
            nationality=valdata['nationality'],
            first_name=valdata['first_name'],
            last_name=valdata['last_name'],
            phone_number=valdata['phone_number'],
            birth_date=valdata['birth_date']
        )
        return user

    class Meta:
        model = User
        fields = ['id', 'url', 'username', 'email', 'password', 'profile_pic', 'nat_id', 'nationality', 'first_name', 'last_name', 'phone_number', 'birth_date']

class PlaceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Place
        fields = ['id', 'url', 'name', 'description', 'location', 'child_friendly', 'opening_times'] #tags

class PackageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Package
        fields = ['id', 'name', 'url', 'place', 'description', 'kind', 'has_tour_guide', 'available', 'opening_times', 'price']
