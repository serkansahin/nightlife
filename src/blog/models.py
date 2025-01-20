import datetime
from django.conf import settings
from django.db import models
from django.template.defaultfilters import slugify
from django.urls import reverse


from events.models import Tag
from nightlife.methods import PathAndRename

# Create your models here.
class BlogPost(models.Model):
    path_and_rename = PathAndRename("blog/")
    title = models.CharField(max_length=255, unique=True, verbose_name="Titre de l'article")
    slug = models.SlugField(max_length=255, unique=True, blank=True)
    created_on = models.DateTimeField(blank=True, null=True)
    last_updated = models.DateTimeField(auto_now=True)
    published = models.BooleanField(default=False, verbose_name="Publié")
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True, related_name="author")
    is_homepage_displayed = models.BooleanField(default=False, verbose_name="Présent sur la page d'accueil")
    summary = models.TextField(blank=True, verbose_name="Sommaire")
    content = models.TextField(blank=True, verbose_name="Contenu")
    thumbnail = models.ImageField(blank=True, upload_to=path_and_rename)
    tags = models.ManyToManyField(Tag, related_name='blogpost_tags')


    class meta:
        ordering = ["-created-on"]
        verbose_name = "Article"

    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)

        return super().save(*args, **kwargs)
    
    #Définir la redirection
    def get_absolute_url(self):
        return reverse("blog:post", kwargs={"slug": self.slug})