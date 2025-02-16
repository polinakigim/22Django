from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name='Email')
    avatar = models.ImageField(upload_to='users/avatars/',blank=True, null=True)
    phone = models.CharField(max_length=15, verbose_name ='Телефон', blank=True, null=True, help_text='Введите номер телефона')
    country = models.CharField(max_length=30, verbose_name ='Телефон', help_text='Укажите страну')


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'Пользователб'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.email