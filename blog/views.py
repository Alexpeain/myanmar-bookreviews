# blog/views.py
from django.views.generic import ListView, DetailView
from .models import Post

class BlogListView(ListView):
    model = Post
    template_name = "blog/blog_list.html"
    context_object_name = "posts"
    ordering = ['-created_at']
    paginate_by = 20  # Number of posts per page
    

class BlogDetailView(DetailView):
    model = Post
    template_name = "blog/blog_detail.html"
    context_object_name = "post"