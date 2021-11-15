from django.db import models


# Create your models here

class Deck(models.Model):
    title = models.CharField(max_length=128)
    description = models.TextField()
    last_reviewed_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.title
