from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """Пользователь."""
    email = models.EmailField(
        verbose_name='Электронная почта',
        unique=True,
        max_length=50
    )
    first_name = models.CharField(
        verbose_name='Имя',
        max_length=30,
    )
    last_name = models.CharField(
        verbose_name='Фамилия',
        max_length=30,
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ('username', 'first_name', 'last_name')

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        constraints = [
            models.UniqueConstraint(
                fields=('username', 'email'),
                name='unique user'
            )
        ]

    def __str__(self):
        return f'{self.last_name} {self.first_name}'
