from django.contrib import admin
from .models import Animal_category, Animal_type
# Register your models here.

class Animal_admin(admin.ModelAdmin):
    list_display = ('animal_type','animal_category','start_date','endDate')

admin.site.register(Animal_category,Animal_admin)

admin.site.register(Animal_type)