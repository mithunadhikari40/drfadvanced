from datetime import date
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import viewsets

from apps.cards.models import Card
from apps.cards.serializer import CardsSerializer
from .models import Deck
from .serializer import DecksSerializer


class DecksViewSet(viewsets.ModelViewSet):
    queryset = Deck.objects.all()
    serializer_class = DecksSerializer


class CardsViewSet(viewsets.ViewSet):
    def list(self, request, decks_pk):
        queryset = Card.objects.filter(deck=decks_pk)
        serializer = CardsSerializer(queryset, many=True)
        return Response(serializer.data)


class TodayCardsViewSet(viewsets.ViewSet):
    def list(self, request, decks_pk):
        """We can import inside the function as well, just like the following commented line"""
        # from datetime import date
        # __day takes day from the datetime because next_review_date is datetime
        queryset = Card.objects.filter(deck=decks_pk, next_review_date__day=date.today().day)
        serializer = CardsSerializer(queryset, many=True)
        return Response(serializer.data)
