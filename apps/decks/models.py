from django.db import models


# Create your models here

class Deck(models.Model):
    title = models.CharField(max_length=128)
    description = models.TextField()
    lastReviewed = models.DateTimeField()
