from django.contrib import admin

# Register your models here.

from .models import UserProfile, Requesters

admin.site.register(Requesters)
admin.site.register(UserProfile)


