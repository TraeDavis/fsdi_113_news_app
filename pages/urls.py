from django.urls import path
from .views import (
    HomePageView,
    ArticleCreateView,
    ArticleUpdateView,
    ArticleDeleteView,
    ArticleDetailView,
    ArticleListView
)

urlpatterns =[
    path("", HomePageView.as_view(), name="home"),
    path("article/new/", ArticleCreateView.as_view(), name="article_new"),
    path("article/list/", ArticleListView.as_view(), name="article_list"),
    path("article/<int:pk>/", ArticleDetailView.as_view(), name="article_detail"),
    path("article/<int:pk>/edit/", ArticleUpdateView.as_view(), name="article_edit"),
    path("article/<int:pk>/delete/", ArticleDeleteView.as_view(), name="article_delete"),

]