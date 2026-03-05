from django.db import models


class Library(models.Model):
    name: str = models.CharField(max_length=100, verbose_name="Название библиотеки")

    location: str = models.CharField(max_length=200, verbose_name="Местоположение")

    website = models.URLField(max_length=200, null=True, blank=True, verbose_name="Сайт библиотеки")

    def __str__(self):
        return self.name



