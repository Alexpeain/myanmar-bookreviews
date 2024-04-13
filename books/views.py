from django.views.generic import ListView,DetailView
from .models import Book
from django.db.models import Q

class BookListView(ListView):
    model = Book
    context_object_name = "book_list"
    template_name = "books/book_list.html"

class BookDetailView(DetailView):
    model = Book
    context_object_name = "book"
    template_name = "books/book_detail.html"
    queryset = Book.objects.all().prefetch_related('reviews__author',)

class SearchResultsListView(ListView):
    model = Book
    context_object_name="book_list"
    template_name ="books/search_results.html"

    def get_queryset(self): # new
        query = self.request.GET.get("q")
        return Book.objects.filter(Q(title__icontains=query) | Q(title__icontains=query)
)