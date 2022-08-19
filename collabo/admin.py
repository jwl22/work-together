from django.contrib import admin
from .models import Project
# Register your models here.

class projectAdmin(admin.ModelAdmin):
    search_fields = ['title']

admin.site.register(Project, projectAdmin)