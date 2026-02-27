from datetime import date

from django.db import models


class Book(models.Model):
    name:str = models.CharField(max_length=100, verbose_name="Название книги")
    author: 'Author' = models.ForeignKey(to='Author', on_delete=models.SET_NULL, null=True, related_name='books')
    published_date:date = models.DateField(verbose_name="Дата публикации")
    library = models.ManyToManyField('library.Library', related_name='books')