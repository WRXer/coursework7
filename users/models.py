from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models


NULLABLE = {'blank': True, 'null': True}

# Create your models here.


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True)
    telegram_username = models.CharField(max_length=100)
    name = models.CharField(max_length=100, verbose_name="имя пользователя", **NULLABLE)
    avatar = models.ImageField(upload_to='users/', verbose_name='аватар', **NULLABLE)
    is_active = models.BooleanField(default=True, verbose_name='подтверждение почты')

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []


    class Meta:
        verbose_name = "пользователь"
        verbose_name_plural = 'пользователи'