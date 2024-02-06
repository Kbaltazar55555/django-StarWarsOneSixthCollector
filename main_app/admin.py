from django.contrib import admin
# import your models here
from .models import SW, Custom, Vehicle

# Register your models here
admin.site.register(SW)
admin.site.register(Custom)
admin.site.register(Vehicle)
