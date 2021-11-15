from rest_framework import serializers
from .models import Deck


class DecksSerializer(serializers.ModelSerializer):
    # title = serializers.CharField(max_length=128)
    # description = serializers.CharField()
    # last_reviewed_date = serializers.DateTimeField()

    """Another way of doing it"""

    class Meta:
        model = Deck
        fields = ['id', 'title', 'description']
