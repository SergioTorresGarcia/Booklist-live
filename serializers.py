from rest_framework import serializers
from .models import Book


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__' # ['title', 'author', 'publishing_year', 'ISBN_number', 'number_of_pages', 'book_cover', 'language']
