from .models import *
from rest_framework import serializers
from rest_framework.reverse import reverse
from rest_framework_simplejwt.settings import api_settings
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.core.exceptions import ObjectDoesNotExist

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
        fields = ['id', 'username', 'email', 'password', 'profile_pic', 'nat_id', 'nationality', 'first_name', 'last_name', 'phone_number', 'birth_date', 'party_count', 'bringing_child']

class PlaceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Place
        fields = ['id', 'url', 'name', 'description', 'location', 'child_friendly', 'opening_times'] #tags

class PackageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Package
        fields = ['id', 'name', 'url', 'place', 'description', 'kind', 'has_tour_guide', 'available', 'opening_times', 'price']

class ReservationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Reservation
        fields = ['booking_number', 'account_id', 'package', 'transaction_date', 'qty', 'price_sum', 'confirmation', 'status']

class LoginSerializer(TokenObtainPairSerializer):

    def validate(self, attrs):
        data = super().validate(attrs)

        refresh = self.get_token(self.user)

        data['user'] = UserSerializer(self.user).data
        data['refresh'] = str(refresh)
        data['access'] = str(refresh.access_token)

        if api_settings.UPDATE_LAST_LOGIN:
            update_last_login(None, self.user)

        return data

class RegisterSerializer(UserSerializer):
    password = serializers.CharField(max_length=128, min_length=8, write_only=True, required=True)
    email = serializers.EmailField(required=True, write_only=True, max_length=128)

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password', 'profile_pic', 'nat_id', 'nationality', 'first_name', 'last_name', 'phone_number', 'birth_date', 'party_count', 'bringing_child']

    def create(self, validated_data):
        try:
            user = User.objects.get(email=validated_data['email'])
        except ObjectDoesNotExist:
            user = User.objects.create_user(**validated_data)
        return user