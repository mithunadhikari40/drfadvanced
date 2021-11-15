from django.db import models

from apps.utils.models import TimeStamps


class Deck(TimeStamps):
    title = models.CharField(max_length=128)
    description = models.TextField()
    last_reviewed_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.title
