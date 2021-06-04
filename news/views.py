from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Article


class ArticleListView(ListView):
    model = Article
    paginate_by = 3
    template_name = 'news.html'


class ArticleDetailView(DetailView):
    model = Article
    template_name = 'article.html'


class ArticleLastView(ListView):
    model = Article
    paginate_by = 3
    template_name = 'lastnews.html'


class ArticleNew():
    pass
