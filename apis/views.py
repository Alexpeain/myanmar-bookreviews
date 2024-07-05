from rest_framework import generics
from books.models import Book
from .serializers import BookSerializer
class BookAPIView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    
class SingleBookView(generics.RetrieveUpdateAPIView,generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
