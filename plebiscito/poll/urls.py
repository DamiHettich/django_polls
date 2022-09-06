from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<int:poll_id>/", views.poll_details, name="poll_details"),
    path("<int:poll_id>/results", views.poll_results, name="poll_results"),
    path("questions/<int:question_id>/", views.question_details, name="question_details"),
    path("questions/<int:question_id>/results", views.question_results, name="question_results"),
    path("questions/<int:question_id>/vote", views.question_vote, name="votes"),

]