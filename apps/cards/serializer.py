from rest_framework import serializers
from .models import Card
from apps.decks.models import Deck

class CardsSerializer(serializers.ModelSerializer):
    # buckets = (
    #     (1, '1 Day'),
    #     (2, '3 Day'),
    #     (3, '7 Day'),
    #     (4, '15 Day'),
    #     (5, '30 Day'),
    # )
    # question = serializers.CharField(max_length=128)
    # answer = serializers.CharField(max_length=1000)
    # """Buckets is now a foreign key to another table, but we could give it a choice very easily"""
    # bucket = serializers.IntegerField(choices=buckets, default=1)
    # next_review_date = serializers.DateTimeField(auto_now_add=True)
    # last_reviewed_date = serializers.DateTimeField(null=True, blank=True)
    #
    """Another way of doing it"""

    # this is not required, only the name of the key is sufficient enough
    deck = serializers.PrimaryKeyRelatedField(queryset=Deck.objects.all())

    class Meta:
        model = Card
        fields = ['id', 'deck', 'question', 'answer']
        # fields = ['id', 'deck', 'question', 'answer', 'bucket', 'next_review_date', 'last_reviewed_date']
