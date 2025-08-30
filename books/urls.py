from django.urls import path,re_path
from . views import BookListView,BookDetailView, SearchResultsListView
from .views import genre_list, genre_index


urlpatterns = [
  path("", BookListView.as_view(), name="book_list"),
  path("book/<path:slug>/", BookDetailView.as_view(), name="book_detail"), # <path:slug> accept unicode mean include burmese except /
  path("search/", SearchResultsListView.as_view(),name="search_results"), # new
  path("genres/<str:name>/", genre_list, name='genre_list'),
  path("genres/", genre_index, name='genre_index'), # new
]