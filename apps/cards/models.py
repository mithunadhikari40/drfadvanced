from django.db import models
from apps.decks.models import Deck


class Buckets(models.Model):
    label = models.TextField(max_length=128)


class Card(models.Model):
    buckets = (
        (1, '1 Day'),
        (2, '3 Day'),
        (3, '7 Day'),
        (4, '15 Day'),
        (5, '30 Day'),
    )
    """One way of referencing"""
    # deck = models.ForeignKey("Deck", on_delete=models.CASCADE)
    deck = models.ForeignKey(Deck, on_delete=models.CASCADE)
    question = models.TextField(max_length=128)
    answer = models.TextField(max_length=1000)
    """Buckets is now a foreign key to another table, but we could give it a choice very easily"""
    # bucket = models.IntegerField(choices=buckets)
    # bucket = models.ForeignKey("Buckets", on_delete=models.CASCADE)
    bucket = models.ForeignKey(Buckets, on_delete=models.CASCADE, default= 1)
    nextReviewDate = models.DateTimeField()
    lastReviewedDate = models.DateTimeField()
