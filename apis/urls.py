from django.urls import path
from .views import BookAPIView,SingleBookView
urlpatterns = [
    path("books/", BookAPIView.as_view(), name="book_list"),   #don't be confuse with books app 
    path('books/<uuid:pk>', SingleBookView.as_view()),
]