from django.contrib import admin

# Register your models here.
from events.models import Tag, Event

class TagAdmin(admin.ModelAdmin):
    list_display = ("name",)

class EventAdmin(admin.ModelAdmin):
    list_display = ("title", "published", "created_on", "last_updated")
    list_editable = ("published",)

admin.site.register(Tag, TagAdmin)
admin.site.register(Event, EventAdmin)