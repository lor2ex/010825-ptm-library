from django.db import models

from library.models.member import Member
from library.models.books import Book
from library.models.library import Library


class Event(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    date = models.DateTimeField()
    library = models.ForeignKey(Library, on_delete=models.CASCADE, related_name='events')
    books = models.ManyToManyField(Book, related_name='events')

    def __str__(self):
        return f"{self.title} {self.library.name} ({self.date})"

    class Meta:
        db_table = "events"
        verbose_name = "Event"
        verbose_name_plural = "Events"


class EventParticipant(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='participants')
    member = models.ManyToManyField(Member, related_name='events')
    registration_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.event.title} ({self.registration_date})"

    class Meta:
        db_table = "event_participants"
        verbose_name = "EventParticipant"
        verbose_name_plural = "EventParticipants"
