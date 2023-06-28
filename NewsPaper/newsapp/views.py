from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post



class PostList(ListView):
    model = Post
    template_name = 'posts.html'
    context_object_name = 'posts'  # имя списка в котором лежат все объекты


class PostDetail(DetailView):
    model = Post
    template_name = 'post.html'
    context_object_name = 'post'  # название объекта
