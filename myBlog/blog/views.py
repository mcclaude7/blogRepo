from django.shortcuts import render
from .models import Article
from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView


class ArticleListView(ListView):
    queryset = Article.objects.all()

def home(request):
    return render(request, 'index.html')
