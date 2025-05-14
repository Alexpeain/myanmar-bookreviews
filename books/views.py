from typing import Any
from django.views.generic import ListView,DetailView
from .models import Book,Genre
from django.db.models import Q
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.core.paginator import Paginator


class BookListView(ListView):
    model = Book
    context_object_name = "book_list"
    paginate_by = 20 #add pagination
    template_name = "books/book_list.html"

    def get_queryset(self):
        queryset = super().get_queryset()
        author = self.request.GET.get("author")
        if author:
            queryset = queryset.filter(author__iexact=author)
        return queryset
    
class BookDetailView(DetailView):
    model = Book
    context_object_name = "book"
    template_name = "books/book_detail.html"
    queryset = Book.objects.all().prefetch_related('reviews__author',)
    
    

class SearchResultsListView(ListView):
    model = Book
    paginate_by = 20
    context_object_name="book_list"
    template_name ="books/search_results.html"

    def get_queryset(self): # new
        query = self.request.GET.get("q")
        return Book.objects.filter(Q(title__icontains=query) | Q(title__icontains=query)
)
def home(request):
    genres = Genre.objects.all()
    return render(request,"home.html",{"genres":genres})

# def books_by_genre(request,genre_name):
#     genre =Genre.objects.get(name=genre_name)
#     books =Book.objects.filter(genre=genre)
#     return render(request,"books/books_by_genre.html",{'genre':genre,'books':books})


def genre_list(request, genre_name):
    genre = get_object_or_404(Genre, name=genre_name)
    books = Book.objects.filter(genres=genre)
    return render(request, 'books/genre_list.html', {'genre': genre, 'books': books})
