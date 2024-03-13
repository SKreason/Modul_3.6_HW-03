from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post


class PostList(ListView):
    model = Post
    ordering = '-dateCreation'
    template_name = 'news.html'
    context_object_name = 'Новости'


class PostDetail(DetailView):
    model = Post
    template_name = 'post.html'
    context_object_name = 'Новость'
