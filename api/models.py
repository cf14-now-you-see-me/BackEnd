from django.db import models
from django.contrib.auth.models import AbstractUser

class PlaceTag(models.Model):
	name = models.CharField(max_length=64)

	def __str__(self):
		return self.name

class Place(models.Model):
	name = models.CharField(max_length=256)
	description = models.CharField(max_length=1024)
	location = models.CharField(max_length=256)
	opening_times = models.CharField(max_length=256, default='')
	tags = models.ManyToManyField(to=PlaceTag, related_name="places")
	child_friendly = models.BooleanField(default=True)
    
	def __str__(self):
		return self.name

class Package(models.Model):
	PACKAGE_TYPES = [
		(0, 'Reguler'),
		(1, 'VIP'),
	]
	name = models.CharField(max_length=256)
	place = models.ForeignKey(Place, on_delete=models.CASCADE)
	description = models.CharField(max_length=1024)
	kind = models.IntegerField(choices=PACKAGE_TYPES, default=0)
	has_tour_guide = models.BooleanField()
	available = models.BooleanField()
	opening_times = models.CharField(max_length=256, default='')
	price = models.IntegerField(default=0)

class PlacePhoto(models.Model):
	description = models.CharField(max_length=512)
	image = models.ImageField(upload_to="static/images", blank=True, null=True)
	place = models.ForeignKey(Place, on_delete=models.CASCADE)

class User(AbstractUser):
	groups = None
	profile_pic = models.ImageField(upload_to="static/avatars", blank=True, null=True)
	# full name