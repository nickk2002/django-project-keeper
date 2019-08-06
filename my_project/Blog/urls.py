from django.urls import path

from .views import (
    article_list_view,
    article_detail_view,
    create_view,
    ArticleListView,
    ArticleDetailView,
    ArticleCreateView
)

app_name = 'Blog'

urlpatterns = [
    path('create/', ArticleCreateView.as_view(), name='blog-create'),
    path('list/', ArticleListView.as_view(), name='blog-list'),
    path('view/<int:id>/', ArticleDetailView.as_view(), name='blog detail')
]
