from datetime import datetime

from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


# Create your models here.

class Author(models.Model):
    name: str = models.CharField(
        max_length=100,
    )
    surname: str = models.CharField(
        max_length=100,
    )
    date_for_birth: datetime = models.DateTimeField()

    profile = models.URLField(
        max_length=100,
        null=True,
        blank=True
    )
    deleted = models.BooleanField(
        default=False
    )
    rating = models.FloatField(
        default=1,
        validators=[
            MinValueValidator(1),
            MaxValueValidator(10)
        ]
    )



