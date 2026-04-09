from django.db import models

from library.models.member import Member
from library.models.books import Book


class Review(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='reviews')
    reviewer = models.ForeignKey(Member, on_delete=models.CASCADE, related_name='reviews')
    rating = models.FloatField()
    description = models.TextField()


    def __str__(self):
        return f"{self.reviewer.last_name} ({self.book.name} {self.rating})"

    class Meta:
        db_table = "reviews"
        verbose_name = "Review"
        verbose_name_plural = "Reviews"
