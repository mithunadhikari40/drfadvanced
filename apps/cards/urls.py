# from rest_framework import routers
from rest_framework_nested import routers
from django.urls import include, path

from .views import CardsViewSet

# router = routers.DefaultRouter()
router = routers.SimpleRouter()
router.register('', CardsViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
