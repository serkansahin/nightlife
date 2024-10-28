from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.db import models

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None):
        if not email:
            raise ValueError("Vous devez rentrer un email")
        email = self.normalize_email(email)
        user = self.model(email=email)
        user.set_password(password)
        user.save()
        return user
    
    def create_superuser(self, email, password=None):
        user = self.create_user(email=email, password=password)
        user.is_admin = True
        user.is_staff = True
        user.save()
        return user

# Create your models here.
class CustomUser(AbstractBaseUser):
    email = models.EmailField(
        unique=True,
        max_length=50,
        blank=False
    )

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    thumbnail = models.ImageField(blank=True, upload_to='users')

    USERNAME_FIELD = 'email'
    #REQUIRED_FIELDS = []
    objects = CustomUserManager()

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True