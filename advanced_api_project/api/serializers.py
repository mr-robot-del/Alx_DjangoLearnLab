from rest_framework import serializers
from .models import Author, Book
from datetime import date

#serializer for the Book Model
#Purpose: Handels serialization/deserialization of book data, including all fields
# Includes custume validation for publication_year to prevent future dates.
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = book
        field ='__all__'

    def validate_publication_year(self, value):
        # custom validation: Ensure year is not in the future.
        # This rund during deserialization (e.g, when creatig/updating a book via Api).
        if value > date.today().year:
            raise serializers.validationError("publication year cannaot be in the future.")
        return value

class AuthorSerializer(serializers.ModelSerializer):
    books = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        Field = ['id', 'name', 'books']
