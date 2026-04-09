from datetime import date
from django.core.validators import MaxValueValidator
from django.db import models
from library.models.publisher import Publisher
from library.models.category import Category


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

    name= models.CharField(max_length=100, verbose_name="Название книги")

    author = models.ForeignKey(
        to='Author',
        on_delete=models.SET_NULL,
        null=True,
        related_name='books'
    )

    published_date = models.DateField(verbose_name="Дата публикации")

    library = models.ManyToManyField('library.Library', related_name='books')

    description= models.TextField(
        verbose_name="Описание книги",
        null=True,
        blank=True
    )

    genre = models.CharField(
        max_length=50,
        verbose_name="Жанр",
        choices=CHOICE_GENRE,
        default='N/A'
    )
    price = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        null=True,
        blank=True
    )
    discounted_price = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        null=True,
        blank=True
    )
    pages = models.PositiveSmallIntegerField(
        validators=[MaxValueValidator(10000)],
        verbose_name="кол-во страниц",
        null=True,
        blank=True
    )
    publisher = models.ForeignKey(
        Publisher,
        on_delete=models.SET_NULL,
        null=True,
        related_name='books'
    )

    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='books',
    )

    def __str__(self):
        return f"{self.name} ({self.genre})"

    @property
    def rating(self):
        reviews = self.reviews.all()
        total_reviews = reviews.count()

        if total_reviews == 0:
            return 0

        total_rating = sum(review.rating for review in reviews)
        average_rating = total_rating / total_reviews

        return round(average_rating, 2)
