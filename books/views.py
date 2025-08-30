from typing import Any
from django.views.generic import ListView,DetailView
from .models import Book,Genre
from django.db.models import Q
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.core.paginator import Paginator
from django.db.models import Count



class BookListView(ListView):
    model = Book
    context_object_name = "book_list"
    paginate_by = 20 #add pagination
    template_name = "books/book_list.html"

    # when request to search for books by author or genre
    # we need to filter the queryset based on the search criteria
    def get_queryset(self):
        queryset = super().get_queryset()
        q = self.request.GET.get("q")
        author = self.request.GET.get("author")
        genre = self.request.GET.get("genre")

        if q:
            queryset = queryset.filter(
                Q(title__icontains=q) |
                Q(author__icontains=q) |
                Q(description__icontains=q)
            )

        if author:
            queryset = queryset.filter(author__iexact=author)
        if genre:
            queryset = queryset.filter(genres__name__iexact=genre) 
        return queryset
    
    # beside object_list : using get_context_data to add additional context
    # to the template
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['genres'] = Genre.objects.all()
        context['authors'] = Book.objects.values_list('author', flat=True).distinct()
        return context
    
class BookDetailView(DetailView):
    model = Book
    context_object_name = "book"
    template_name = "books/book_detail.html"
    queryset = Book.objects.all().prefetch_related('reviews__author',)
    
    

class SearchResultsListView(ListView):
    model = Book
    template_name = 'search_results.html'
    context_object_name = 'book_list'
    paginate_by = 20

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            # Normalize the user's query by removing all spaces for robust searching
            cleaned_query = query.strip().replace(" ", "")

            # Search across multiple fields using Q objects for an OR lookup
            return Book.objects.filter(
                Q(title__icontains=cleaned_query) |
                Q(author__icontains=cleaned_query) |
                Q(title_searchable__icontains=cleaned_query)
            ).order_by('title')  # Order the results to ensure consistent pagination

        # Return an empty queryset if no search query is provided
        return Book.objects.none()
    
def home(request):
    # genres = Genre.objects.all()
    genres = Genre.objects.annotate(book_count=Count("book"))
    return render(request,"home.html",{"genres":genres})

# def books_by_genre(request,genre_name):
#     genre =Genre.objects.get(name=genre_name)
#     books =Book.objects.filter(genre=genre)
#     return render(request,"books/books_by_genre.html",{'genre':genre,'books':books})


def genre_list(request, name):
    genre = get_object_or_404(Genre, name= name)
    books = Book.objects.filter(genres=genre)
    return render(request, 'books/genre_list.html', {'genre': genre, 'books': books})

def genre_index(request):
    return render(request, "books/genre_index.html", {"genres": Genre.objects.all()})
    