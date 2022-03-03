from django.views.generic import ListView, DetailView
from articles.models import Article

# Create your views here.

class ArticlesListView(ListView):
  template_name = "articles.html"
  model = Article

class ArticlesDetailView(DetailView):
  template_name = "articles_detail.html"
  model = Article




