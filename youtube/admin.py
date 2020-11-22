from django.contrib import admin
from .models import Youtube_file


@admin.register(Youtube_file)
class Youtube_fileAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'title', 'url']