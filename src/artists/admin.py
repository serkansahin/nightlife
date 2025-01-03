from django.contrib import admin

# Register your models here.
from artists.models import Artist

class ArtistAdmin(admin.ModelAdmin):
    list_display = ['name', 'published', 'created_on', 'last_updated', 'spotify', 'soundcloud','instagram','facebook']
    list_editable = ['published',]

admin.site.register(Artist, ArtistAdmin)