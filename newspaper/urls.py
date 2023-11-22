from django.urls import path, include

from newspaper.views import (
    NewspaperListView,
    NewspaperDetailView,
    RedactorListView,
    TopicListView,
)

urlpatterns = [
    path("", NewspaperListView.as_view(), name="newspaper-list"),
    path("article/<int:pk>/", NewspaperDetailView.as_view(), name="newspaper-detail"),
    path("redactors/", RedactorListView.as_view(), name="redactor-list"),
    path("topics/", TopicListView.as_view(), name="topic-list"),
]

app_name = "newspaper"
