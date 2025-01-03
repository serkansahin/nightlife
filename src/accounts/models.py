from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.db import models

from django.template.defaultfilters import slugify
from django.urls import reverse

from nightlife.methods import PathAndRename

class CustomUserManager(BaseUserManager):
    def create_user(self, email, username, town, thumbnail, password=None):
        if not email:
            raise ValueError("Vous devez rentrer un email")
        email = self.normalize_email(email)
        user = self.model(
            email=email,
            username=username,
            town=town,
            thumbnail=thumbnail,
            )
        user.is_promoter = False
        user.set_password(password)
        user.save()
        return user
    
    def create_promoter(self, email, username, town, thumbnail, biography, password=None):
        if not email:
            raise ValueError("Vous devez rentrer un email")
        email = self.normalize_email(email)
        user = self.model(
            email=email,
            username=username,
            town=town,
            thumbnail=thumbnail,
            biography=biography,
            )
        user.is_promoter = True
        user.set_password(password)
        user.save()
        return user
    
    def create_superuser(self, email, username, town, thumbnail, password=None):
        email = self.normalize_email(email)
        user = self.create_user(
            email=email,
            username=username,
            town=town,
            thumbnail=thumbnail,
            password=password
        )
        user.is_admin = True
        user.is_promoter = True
        user.save()
        return user

# Create your models here.
class CustomUser(AbstractBaseUser):
    path_and_rename = PathAndRename("users/")

    email = models.EmailField(
        unique=True,
        max_length=50,
        blank=False,
        verbose_name="Email"
    )
    username = models.CharField(max_length=15, unique=True, blank=False, verbose_name="Votre nom / pseudo")
    slug = models.SlugField(max_length=15, unique=True)
    town = models.CharField(max_length=30, null=True, verbose_name="Ville")
    thumbnail = models.ImageField(blank=True, upload_to=path_and_rename)
    is_active = models.BooleanField(default=True)
    is_promoter = models.BooleanField(default=False, verbose_name="Êtes-vous organisateur ?")
    is_admin = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = [email, username]
    objects = CustomUserManager()

    @property
    def is_staff(self):
        return self.is_admin

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True
    
    def __str__(self):
        return self.username
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.username)

        return super().save(*args, **kwargs)
    
    #Définir la redirection
    def get_absolute_url(self):
        return reverse("accounts:userdetails", kwargs={"slug": self.slug})