# apis/serializers.py
from rest_framework import serializers
from books.models import Book,Review
import bleach
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['Bid',"title","author","description"]
    
class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['book','review','author']

    #using clean/bleach to remove all HTML tags from review field preventing XSS attacks
    def validate_review(self, value):
        cleaned_value = bleach.clean(value, tags=[], strip=True)
        if len(cleaned_value) < 10:
            raise serializers.ValidationError("Review must be at least 10 characters long after cleaning.") 
        
        return cleaned_value