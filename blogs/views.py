from django.views.generic import ListView, DetailView
from .models import Post


class PostListView(ListView):
    """List all blog posts"""
    model = Post
    template_name = 'blogs/home.html'
    context_object_name = 'posts'

class PostDetailView(DetailView):
    """Show details of a post"""
    model = Post
    template_name = 'blogs/detail.html'
