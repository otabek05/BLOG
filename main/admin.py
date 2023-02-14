from django.contrib import admin

from .models import Todo


@admin.register(Todo)
class TodoAdmin(admin.ModelAdmin):
    list_display = ['id', 'owner', 'body', 'completed']
    list_display_links = ['id']
    list_filter = ['created', 'updated']
    search_fields = ['owner__username', 'body']
    list_editable = ['body', 'completed']
