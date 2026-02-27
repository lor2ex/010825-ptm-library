from datetime import datetime

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



