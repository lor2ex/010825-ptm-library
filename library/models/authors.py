from datetime import datetime

from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


class Author(models.Model):
    name: str = models.CharField(
        max_length=100,
        verbose_name="Имя"
    )
    surname: str = models.CharField(
        max_length=100,
        verbose_name="Фамилия"

    )
    date_for_birth: datetime = models.DateTimeField(
        verbose_name="Дата рождения"

    )

    profile = models.URLField(
        max_length=100,
        null=True,
        blank=True,
        verbose_name="Ссылка на личную страницу"

    )
    deleted = models.BooleanField(
        default=False,
        verbose_name="Удален",
        help_text="Отметьте, если автор помечен как неактивный"

    )
    rating = models.FloatField(
        default=1,
        validators=[
            MinValueValidator(1),
            MaxValueValidator(10)
        ],
        verbose_name="Рейтинг"

    )

    def __str__(self):
        return f"{self.surname} {self.name[0]} ({self.rating})"