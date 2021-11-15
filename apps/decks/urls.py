# from rest_framework import routers
from rest_framework_nested import routers
from django.urls import include, path

from .views import DecksViewSet, CardsViewSet, TodayCardsViewSet

# router = routers.DefaultRouter()

router = routers.SimpleRouter()
router.register('', DecksViewSet)

cards_router = routers.NestedSimpleRouter(router, r'', lookup='decks')
cards_router.register('cards', CardsViewSet, basename='deck_cards')
# to get the cards from a deck where the passed date matches the date on the card, `last_review_at`
today_cards_router = routers.NestedSimpleRouter(router, r'', lookup='decks')
today_cards_router.register(r'today_cards', TodayCardsViewSet, basename='today_cards')

urlpatterns = [
    path('', include(router.urls)),
    path('', include(cards_router.urls)),
    path('', include(today_cards_router.urls)),

]
