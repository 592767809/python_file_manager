from django.contrib import admin

# Register your models here.

from apikey.models import ApiKey

admin.site.register(ApiKey)
