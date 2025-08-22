from django.urls import path
from . views import BookListView,BookDetailView, SearchResultsListView
from .views import genre_list


urlpatterns = [
  path("", BookListView.as_view(), name="book_list"),
  path("<slug:slug>", BookDetailView.as_view(), name="book_detail"),
  path("search/", SearchResultsListView.as_view(),name="search_results"), # new
  path('genres/<str:genre_name>/', genre_list, name='genre_list'),
]