from django.contrib import admin
from user.models import Profile
from user.models import Car
from user.models import Rental
# Register your models here.

admin.site.register(Profile)
admin.site.register(Car)
admin.site.register(Rental)