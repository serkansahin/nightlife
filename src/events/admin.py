from django.contrib import admin

# Register your models here.
from events.models import Event

class EventAdmin(admin.ModelAdmin):
    list_display = ("title", "published", "created_on", "last_updated")
    list_editable = ("published",)

admin.site.register(Event, EventAdmin)