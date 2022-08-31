from django.db import models
from django.contrib.auth.models import AbstractUser

class PlaceTag(models.Model):
	name = models.CharField(max_length=64)

	def __str__(self):
		return self.name

class Place(models.Model):
	name = models.CharField(max_length=255)
	description = models.CharField(max_length=1024)
	location = models.CharField(max_length=255)
	price = models.IntegerField(default=0)
	tags = models.ManyToManyField(to=PlaceTag, related_name="places")

class PlacePhoto(models.Model):
	description = models.CharField(max_length=512)
	image = models.ImageField(upload_to="images", blank=True, null=True)
	place = models.ForeignKey(Place, on_delete=models.CASCADE)

class User(AbstractUser):
	groups = None
	profile_pic = models.ImageField(upload_to="avatars", blank=True, null=True)