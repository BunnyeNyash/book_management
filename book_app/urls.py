# Map URLs to the view
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookViewSet

router = DefaultRouter()
router.register(r'api/books', BookViewSet, basename='book')

urlpatterns = [
    path('', include(router.urls)),
]
