from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Post

# Create your views here.

class HomeView(ListView):
    template_name = 'home.html'
    model = Post

class PostDetailView(DetailView):
    template_name = 'post_detail.html'
    model = Post

class PostesView(ListView):
    template_name = 'postes.html'
    model = Post

class PostCreateView(CreateView):
    template_name = 'post_create.html'
    model = Post
    fields = ['title', 'author', 'body']

class PostUpdateView(UpdateView):
    template_name = 'post_update.html'
    model = Post
    fields = ['title', 'author', 'body']

class PostDeleteView(DeleteView):
    template_name = 'post_delete.html'
    model = Post
    success_url = reverse_lazy('postes')