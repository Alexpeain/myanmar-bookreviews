from django.views.generic import TemplateView
from books.models import Book

class HomePageView(TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['book_list'] = Book.objects.all().prefetch_related('reviews')
        return context

class AboutPageView(TemplateView): # new
    template_name = "about.html"