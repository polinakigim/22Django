from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    username = models.CharField(max_length=50, default="default_user")
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    avatar = models.ImageField(upload_to="users/avatars/", blank=True, null=True)
    country = models.CharField(max_length=100, blank=True, null=True)

    USERNAME_FIELD = 'email'  # Логинимся по email
    REQUIRED_FIELDS = ["username"]  # Указываем, что username обязателен

    def __str__(self):
        return self.email

