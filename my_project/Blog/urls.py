from django.urls import path

from .views import (
    ArticleListView,
    ArticleDetailView,
    ArticleCreateView,
    ArticleUpdateView,
    ArticleDeleteView,
    home_view,
    register_view
)

app_name = "blog"

urlpatterns = [
    path('', home_view, name='blog-home'),
    path('register/', register_view, name='blog-register'),
    path('create/', ArticleCreateView.as_view(), name='blog-create'),
    path('list/', ArticleListView.as_view(), name='blog-list'),
    path('view/<int:id>/', ArticleDetailView.as_view(), name='blog-detail'),
    path('update/<int:id>/', ArticleUpdateView.as_view(), name='blog-update'),
    path('delete/<int:id>/', ArticleDeleteView.as_view(), name='blog-delete'),
]
