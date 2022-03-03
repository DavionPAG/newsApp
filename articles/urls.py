from django.urls import path
from .views import (
  ArticlesListView, 
  ArticlesDetailView,
  )

urlpatterns = [
  path('articles/', ArticlesListView.as_view(), name='articles_list'),
  path('articles/<int:pk>/', ArticlesDetailView.as_view(), name="articles_details"),
]