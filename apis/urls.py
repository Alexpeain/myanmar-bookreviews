from django.urls import path
from .views import BookAPIView,SingleBookView,ReviewAPIView
urlpatterns = [
    path("books/", BookAPIView.as_view(), name="book_list"),   #don't be confuse with books app 
    path('books/<uuid:pk>', SingleBookView.as_view()),
    path("reviews/", ReviewAPIView.as_view(), name="review_list"),

]