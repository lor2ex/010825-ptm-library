from datetime import date
from django.core.validators import MaxValueValidator
from django.db import models


class Category(models.Model):
    name: str = models.CharField(
        max_length=30,
        verbose_name="Имя категории",
        unique=True
    )


class Book(models.Model):
    CHOICE_GENRE = [
        ("N/A", "Not Selected"),
        ('Fiction', 'Fiction'),
        ('Non-Fiction', 'Non-Fiction'),
        ('Science Fiction', 'Science Fiction'),
        ('Fantasy', 'Fantasy'),
        ('Mystery', 'Mystery'),
        ('Biography', 'Biography'),
    ]

    name:str = models.CharField(max_length=100, verbose_name="Название книги")
    author: 'Author' = models.ForeignKey(to='Author', on_delete=models.SET_NULL, null=True, related_name='books')
    published_date:date = models.DateField(verbose_name="Дата публикации")
    library = models.ManyToManyField('library.Library', related_name='books')
    description: str = models.TextField(verbose_name="Описание книги", null=True, blank=True)
    genre: str = models.CharField(max_length=50, verbose_name="Жанр", choices=CHOICE_GENRE, default='N/A')
    pages: int = models.PositiveSmallIntegerField(validators=[MaxValueValidator(10000)], verbose_name="кол-во страниц", null=True, blank=True)
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