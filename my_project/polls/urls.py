from django.urls import path

from .views import (
    questions_list_view,
    question_detail_view,
    question_vote_view,
    results_view,
    choice_create_view
)

app_name = 'polls' # namespace url names

urlpatterns = [

    path('', questions_list_view, name="index"),
    path('<int:question_id>/', question_detail_view, name="detail"),
    path('<int:question_id>/vote', question_vote_view, name="vote"),
    path('<int:question_id>/results', results_view, name="results"),
    path('<int:question_id>/create_choice', choice_create_view, name="create choice"),
    # path('<int:question_id>/delete/<int:choice_id>/')
]
