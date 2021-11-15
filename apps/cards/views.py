from django.shortcuts import render

from rest_framework import viewsets, permissions
from .models import Card
from .serializer import CardsSerializer


class CardsViewSet(viewsets.ModelViewSet):
    queryset = Card.objects.all()
    serializer_class = CardsSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
