from django.shortcuts import render
from django.views.generic import ListView, DetailView, FormView, CreateView
from .models import Article
from .forms import AddPost
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.http import HttpResponse


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


@method_decorator(login_required, name='dispatch')
class NewsManager(CreateView):
    form_class = AddPost(author=request.user)
    template_name = 'adminpanel.html'
    success_url = '/news/'
