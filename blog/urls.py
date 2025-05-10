from django.urls import path
from . import views

urlpatterns = [
    path('', views.blog_list, name='blog_home'),  # or whatever your main blog view is
]
