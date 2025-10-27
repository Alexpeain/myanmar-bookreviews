from rest_framework import generics
from books.models import Book,Review
from .serializers import BookSerializer,ReviewSerializer
class BookAPIView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    
class SingleBookView(generics.RetrieveUpdateAPIView,generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class ReviewAPIView(generics.ListCreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer