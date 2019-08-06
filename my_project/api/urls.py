from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import detail_view, list_view

app_name = "api"

urlpatterns = [
    path('', list_view, name="home"),
    path('detail/<int:id>/', detail_view, name="detail")
]

urlpatterns = format_suffix_patterns(urlpatterns)