from django.contrib import admin
from .models import *


class LaptopPhotosInline(admin.TabularInline):
    model = LaptopPhoto
    extra = 1


class LaptopAdmin(admin.ModelAdmin):
    inlines = [LaptopPhotosInline]


admin.site.register(Laptop, LaptopAdmin)
