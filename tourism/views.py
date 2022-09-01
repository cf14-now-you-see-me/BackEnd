from django.shortcuts import render
from django.http import HttpResponse

from .models import User, Place
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import UserSerializer, PlaceSerializer

# Create your views here.

def index(request):
    return HttpResponse("index")

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

class PlaceViewSet(viewsets.ModelViewSet):
    queryset = Place.objects.all()
    serializer_class = PlaceSerializer
    permission_classes = [permissions.IsAuthenticated]