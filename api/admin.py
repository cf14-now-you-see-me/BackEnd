from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(PlaceTag)
admin.site.register(Place)
admin.site.register(Package)
admin.site.register(PlacePhoto)
admin.site.register(User)