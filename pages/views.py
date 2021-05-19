from django.views.generic import ListView, DetailView
from django.views.generic.edit import (
    CreateView,
    UpdateView, 
    DeleteView
)
from .models import Article
from .forms import ArticleForm
from django.urls import reverse_lazy
from accounts.models import CustomUser

class HomePageView(ListView):
    model = Article
    template_name = 'home.html'

class ArticleDetailView(DetailView):
    model = Article
    template_name = "article_detail.html"

class ArticleCreateView(CreateView):
    model = Article
    form_class = ArticleForm
    template_name = 'article_new.html'
    

class ArticleUpdateView(UpdateView):
    model = Article
    template_name = "article_edit.html"
    fields = ["title", "body"]

class ArticleDeleteView(DeleteView):
    model = Article
    template_name = "article_delete.html"
    success_url = reverse_lazy("home")
