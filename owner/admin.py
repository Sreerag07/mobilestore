from django.contrib import admin
from .models import Brand,Mobile
# Register your models here.

admin.site.register(Brand)
admin.site.register(Mobile)

#manage.py createsuperuser