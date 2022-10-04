from django.contrib import admin
from .models import APIoperation
# Register your models here.

@admin.register(APIoperation)
class APIoperationAdmin(admin.ModelAdmin):
    list_display= ['id', 'create', 'update', 'retrieve', 'delete']
