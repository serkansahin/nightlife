from django import forms

from artists.models import Artist

class ArtistCreateForm(forms.ModelForm):
    class Meta:
        model = Artist
        fields = ["name", "biography",]