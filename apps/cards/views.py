from django.shortcuts import render

from rest_framework import viewsets
from .models import Card
from .serializer import CardsSerializer


class CardsViewSet(viewsets.ModelViewSet):
    queryset = Card.objects.all()
    serializer_class = CardsSerializer
