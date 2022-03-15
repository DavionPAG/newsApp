from articles.models import Article
from django.views.generic import ListView, DetailView
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

# Create your views here.

class ArticlesListView(ListView):
  template_name = "articles/articles_list.html"
  model = Article

class ArticleDetailView(DetailView):
  template_name = "articles/article_details.html"
  model = Article

class ArticleCreateView(LoginRequiredMixin, CreateView):
  template_name = 'articles/new_article.html'
  model = Article
  fields = ['title', 'author', 'body']

class ArticleUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
  template_name = 'articles/article_update.html'
  model = Article
  fields = ['title', 'body']
  
  def test_func(self):
    obj = self.get_object()
    return obj.author == self.request.user

class ArticleDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
  template_name = 'articles/article_delete.html'
  model = Article
  success_url = reverse_lazy('articles_list')

  def test_func(self):
    obj = self.get_object()
    return obj.author == self.request.user


