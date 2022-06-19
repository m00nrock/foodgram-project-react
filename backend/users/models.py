from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    username = models.CharField(
        'Уникальное имя',
        db_index=True,
        max_length=150,
        unique=True,
        help_text='Введите уникальное имя пользователя')
    email = models.EmailField(
        'Электронная почта',
        db_index=True,
        unique=True,
        max_length=254,
        help_text='Введите электронную почту пользователя')
    first_name = models.CharField(
        'Имя',
        max_length=150,
        help_text='Введите имя пользователя')
    last_name = models.CharField(
        'Фамилия',
        max_length=150,
        help_text='Введите фамилию пользователя')
    is_subscribed = models.BooleanField(
        default=False,
        verbose_name='Подписка на данного пользователя',
        help_text='Отметьте для подписки на данного пользователя')
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name', 'password']

    def __str__(self):
        return self.username
