from datetime import date
from django.db import models


class Category(models.Model):
    name: str = models.CharField(
        max_length=30,
        verbose_name="Имя категории",
        unique=True
    )


class Book(models.Model):
    name: str = models.CharField(max_length=100, verbose_name="Название книги")
    author: 'Author' = models.ForeignKey(
        to='Author',
        on_delete=models.SET_NULL,
        null=True,
        related_name='books'
    )
    published_date: date = models.DateField(verbose_name="Дата публикации")
    category: 'Category' = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True,
        related_name='books'
    )


"""Создайте модель Category для хранения категорий книг. Модель будет содержать поля:
Имя категории: макс. длина 30, категории должны быть уникальны

Свяжите модель Category с моделью Book с помощью связи "один ко многим"
У книги должна быть возможность получить сведения о категории по “относящемуся имени”.
Одна категория может быть у многих различных книг. Каждая книга может состоять только в 
одной категории (для примера: Книга из категории “Для размышлений”, 
жанр - “Психологический детектив”)."""