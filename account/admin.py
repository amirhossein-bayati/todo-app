from django.contrib import admin
from .models import Task


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'created', 'complete')
    list_filter = ('user', 'complete')
    search_fields = ('title', 'description')
    ordering = ('user', 'complete', 'created')