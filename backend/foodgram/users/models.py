from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """Custom user model."""
    username = models.CharField(
        db_index=True,
        max_length=150,
        unique=True
    )
    email = models.EmailField(
        db_index=True,
        max_length=150,
        unique=True
    )
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    is_subscribed = models.BooleanField(default=False)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'password', 'first_name', 'last_name']

    def __str__(self):
        return self.username
