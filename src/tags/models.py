from django.db import models
from django.utils.text import slugify

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