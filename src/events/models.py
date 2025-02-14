import datetime
from django.conf import settings
from django.db import models
from django.contrib.auth import get_user_model
from django.template.defaultfilters import slugify
from django.urls import reverse

from artists.models import Artist
from nightlife.methods import PathAndRename

# Create your models here.
class Tag(models.Model):
    name = models.CharField(max_length=255, unique=True, verbose_name="tag")
    slug = models.SlugField(max_length=255, unique=True)

    class Meta:
        ordering = ["name"]
    
    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
 
        return super().save(*args, **kwargs)
    
class Comment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="comments")
    comment = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_on"]
        verbose_name = "Commentaire"

    def __str__(self):
        return self.comment
    
class Event(models.Model):
    path_and_rename = PathAndRename("events/")

    title = models.CharField(max_length=255, unique=True, verbose_name="Titre")
    slug = models.SlugField(max_length=255, unique=True, blank=True)
    created_on = models.DateTimeField(blank=True, null=True)
    last_updated = models.DateTimeField(auto_now=True)
    starts = models.DateTimeField(verbose_name="Début")
    ends = models.DateTimeField(verbose_name="Fin")
    published = models.BooleanField(default=False, verbose_name="Publié")
    is_sponsored = models.BooleanField(default=False, verbose_name="Sponsorisé")
    promoter = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True, related_name="promoter")
    location = models.CharField(max_length=255, null=True, blank=True, verbose_name="Localisation")
    address = models.CharField(max_length=255, null=True, blank=True, verbose_name="Adresse")
    town = models.CharField(max_length=255, null=True, blank=True, verbose_name="Ville")
    price = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True, verbose_name="Prix")
    content = models.TextField(blank=True, verbose_name="Contenu")
    thumbnail = models.ImageField(blank=True, upload_to=path_and_rename)
    artists = models.ManyToManyField(Artist, related_name="events")
    interested = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="interested")
    tags = models.ManyToManyField(Tag, related_name='event_tags', blank=True)
    comments = models.ManyToManyField(Comment, related_name='event_comment', blank=True)

    class Meta:
        ordering = ["-created_on"]
        verbose_name = "Event"

    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)

        return super().save(*args, **kwargs)
    
    #Définir la redirection
    def get_absolute_url(self):
        return reverse("events:event", kwargs={"slug": self.slug})

    def total_interested(self):
        return self.interested.count()