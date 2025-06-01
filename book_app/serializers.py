from rest_framework import serializers
from .models import Book
from datetime import date

class BookSerializer(serializers.ModelSerializer):
    days_since_published = serializers.SerializerMethodField()

    class Meta:
        model = Book
        fields = ['id', 'title', 'author', 'published_date', 'genre', 'days_since_published']

    def get_days_since_published(self, obj):
        today = date.today()
        delta = today - obj.published_date
        return delta.days
