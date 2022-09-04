from django.urls import path, include
from . import views

from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'places', views.PlaceViewSet)
router.register(r'package', views.PackageViewSet)
router.register(r'reservation', views.ReservationViewSet)
router.register(r'auth/login', views.LoginViewSet, basename='auth-login')
router.register(r'auth/register', views.RegistrationViewSet, basename='auth-register')
router.register(r'auth/refresh', views.RefreshViewSet, basename='auth-refresh')

urlpatterns = [
	path("", include(router.urls)),
	path("api-auth/", include('rest_framework.urls', namespace='rest_framework'))
]
