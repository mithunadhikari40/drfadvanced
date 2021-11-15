from django.shortcuts import render

from rest_framework import viewsets
from .models import Deck
from .serializer import DecksSerializer


class DecksViewSet(viewsets.ModelViewSet):
    queryset = Deck.objects.all()
    serializer_class = DecksSerializer
