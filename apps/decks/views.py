from django.shortcuts import render
from rest_framework.response import Response

from apps.cards.models import Card
from apps.cards.serializer import CardsSerializer

from rest_framework import viewsets
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

