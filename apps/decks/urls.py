# from rest_framework import routers
from rest_framework_nested import routers
from django.urls import include, path

from .views import DecksViewSet, CardsViewSet

# router = routers.DefaultRouter()

router = routers.SimpleRouter()
router.register('', DecksViewSet)


cards_router = routers.NestedSimpleRouter(router, r'', lookup='decks')
cards_router.register('cards', CardsViewSet, basename='deck_cards')

urlpatterns = [
    path('', include(router.urls)),
    path('', include(cards_router.urls))

]
