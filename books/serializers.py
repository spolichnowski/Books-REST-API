from rest_framework import serializers
from .models import Author, Book, Category


class BookSerializer(serializers.ModelSerializer):
    authors = serializers.StringRelatedField(many=True, read_only=True)
    categories = serializers.StringRelatedField(many=True, read_only=True)

    class Meta:
        model = Book
        fields = [
            'book_id',
            'title',
            'authors',
            'published_date',
            'categories',
            'average_rating',
            'ratings_count',
            'thumbnail'
        ]


class DetailBookSerializer(serializers.ModelSerializer):
    authors = serializers.StringRelatedField(many=True, read_only=True)
    categories = serializers.StringRelatedField(many=True, read_only=True)

    class Meta:
        model = Book
        lookup_field = 'book_id'
        fields = [
            'title',
            'authors',
            'published_date',
            'categories',
            'average_rating',
            'ratings_count',
            'thumbnail'
        ]
