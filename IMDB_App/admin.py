from django.contrib import admin

# Register your models here.
from .models import *
Data_Models=[Movie,Actor,Director,Cast,Rating,Genre]
admin.site.register(Data_Models)