from django.contrib import admin
from .models import *


@admin.register(CarModel)
class CarModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'brand', 'model', 'price']
    ordering = ('brand',)


