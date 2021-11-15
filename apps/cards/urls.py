from rest_framework import routers
from django.urls import include, path

from .views import CardsViewSet

router = routers.DefaultRouter()
router.register('', CardsViewSet)
urlpatterns = [
    path('', include(router.urls))
]
