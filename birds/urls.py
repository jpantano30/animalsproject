from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BirdViewSet

router = DefaultRouter()
router.register(r'', BirdViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
