# Handles API requests
from django.shortcuts import render
from rest_framework import viewsets
from .models import Book
from .serializers import BookSerializer

# Uses a ViewSet for multiple actions (list, create, retrieve, update, delete)
class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def get_view_name(self):
        return "Book List Create Api"
