from django.contrib import admin

from areas.models import Area


@admin.register(Area)
class AreaAdmin(admin.ModelAdmin):
    list_display = ["title", "thumbnail_url", "modified"]
    readonly_fields = ["created", "modified"]
    fieldsets = [
        (None, {"fields": ["title", "description", "thumbnail_url"]}),
        ("System", {"classes": ["collapse"], "fields": ["created", "modified"]}),
    ]
    ordering = ["-modified"]
