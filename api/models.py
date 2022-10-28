from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone

class PlaceTag(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name

class Place(models.Model):
    name = models.CharField(max_length=256)
    description = models.CharField(max_length=2048)
    google_id = models.CharField(max_length=256)
    location = models.CharField(max_length=256)
    child_friendly = models.BooleanField(default=True)
    ticket_price = models.CharField(max_length=256, default='')
    opening_times = models.CharField(max_length=256, default='')
    tags = models.ManyToManyField(to=PlaceTag, related_name="places")
    long_description = models.CharField(max_length=4096, default='')
    
    def __str__(self):
        return self.name

class Amenity(models.Model):
    AMENITY_TYPES = [
        (0, 'Inn'),
        (1, 'Restaurant')
    ]
    name = models.CharField(max_length=256)
    kind = models.IntegerField(choices=AMENITY_TYPES, default=0)
    google_id = models.CharField(max_length=256, default='')
    info = models.CharField(max_length=4096)
    near = models.ForeignKey(Place, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name
# class Package(models.Model):
#     PACKAGE_TYPES = [
#         (0, 'Reguler'),
#         (1, 'VIP'),
#     ]
#     name = models.CharField(max_length=256)
#     place = models.ForeignKey(Place, on_delete=models.CASCADE)
#     description = models.CharField(max_length=1024)
#     kind = models.IntegerField(choices=PACKAGE_TYPES, default=0)
#     has_tour_guide = models.BooleanField()
#     available = models.BooleanField()
#     opening_times = models.CharField(max_length=256, default='')
#     price = models.IntegerField(default=0)

#     def __str__(self):
#         return ' '.join([self.name, '(%s)' % self.PACKAGE_TYPES[self.kind][1]])

# class PlacePhoto(models.Model):
#     description = models.CharField(max_length=512)
#     image = models.ImageField(upload_to="static/images", blank=True, null=True)
#     place = models.ForeignKey(Place, on_delete=models.CASCADE)

# class User(AbstractUser):
#     profile_pic = models.ImageField(upload_to="static/avatars", blank=True, null=True)
#     nationality = models.CharField(max_length=256, default='-')
#     birth_date = models.DateField(default=timezone.now)
#     nat_id = models.IntegerField(default=0)
#     phone_number = models.IntegerField(default=0)
#     party_count = models.IntegerField(default=1)
#     bringing_child = models.BooleanField(default=False)

# class Reservation(models.Model):
#     CONFIRMATION_STATUS = [
#         (0, 'Waiting'),
#         (1, 'Confirmed'),
#         (2, 'Cancelled'),
#     ]
#     booking_number = models.IntegerField()
#     account_id = models.IntegerField()
#     package = models.ForeignKey(Package, on_delete=models.CASCADE)
#     transaction_date = models.DateTimeField(default=timezone.now)
#     qty = models.IntegerField()
#     price_sum = models.IntegerField()
#     confirmation = models.CharField(max_length=256, null=True)
#     status = models.IntegerField(choices=CONFIRMATION_STATUS, default=0)
