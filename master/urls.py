from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .api.common import CountryViewSet

router = DefaultRouter()
router.register('country', CountryViewSet, basename='country')


urlpatterns = [
    path('', include(router.urls)),
]
