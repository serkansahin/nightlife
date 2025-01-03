import datetime
from django.db import models
from django.template.defaultfilters import slugify
from django.urls import reverse


from nightlife.methods import PathAndRename

# Create your models here.
class Artist(models.Model):
    path_and_rename = PathAndRename("artists/")
    name = models.CharField(max_length=255, unique=True, verbose_name="Nom de l'artiste")
    slug = models.SlugField(max_length=255, unique=True, blank=True)
    created_on = models.DateTimeField(blank=True, null=True)
    last_updated = models.DateTimeField(auto_now=True)
    published = models.BooleanField(default=False, verbose_name="Publié")
    is_sponsored = models.BooleanField(default=False, verbose_name="Sponsorisé")
    biography = models.TextField(blank=True, verbose_name="Biographie")
    thumbnail = models.ImageField(blank=True, upload_to=path_and_rename)
    spotify = models.URLField(max_length=255, unique=True, blank=True)
    soundcloud = models.URLField(max_length=255, unique=True, blank=True)
    instagram = models.URLField(max_length=255, unique=True, blank=True)
    facebook = models.URLField(max_length=255, unique=True, blank=True)


    class meta:
        ordering = ["-created-on"]
        verbose_name = "Artiste"

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)

        return super().save(*args, **kwargs)
    
    #Définir la redirection
    def get_absolute_url(self):
        return reverse("artists:artist", kwargs={"slug": self.slug})