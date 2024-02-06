from django.contrib import admin
# import your models here
from .models import SW, Custom

# Register your models here
admin.site.register(SW)
admin.site.register(Custom)
