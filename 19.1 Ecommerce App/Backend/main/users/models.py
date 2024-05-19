from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

from users.managers import CustomUserManager

# from .managers import CustomUserManager


class CustomUser(AbstractBaseUser):
    email = models.EmailField(verbose_name='email address', unique=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    last_login= models.DateTimeField(auto_now=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email
