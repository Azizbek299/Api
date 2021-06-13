from django.contrib import admin
from .models import *


@admin.register(Boglanish)
class BoglanishAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'phone')
    list_display_links = ('name', 'phone')


@admin.register(PhoneNumber)
class PhoneNumberAdmin(admin.ModelAdmin):
    list_display = ('id', 'phone_number')
    list_display_links = ('phone_number',)
