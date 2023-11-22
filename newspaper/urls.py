from django.urls import path, include

from newspaper.views import (
    NewspaperListView,
    NewspaperDetailView,
    RedactorListView,
    TopicListView,
    TopicCreateView,
    TopicDeleteView,
    TopicUpdateView,
)

urlpatterns = [
    path("", NewspaperListView.as_view(), name="newspaper-list"),
    path("article/<int:pk>/", NewspaperDetailView.as_view(), name="newspaper-detail"),
    path("redactors/", RedactorListView.as_view(), name="redactor-list"),
    path("topics/", TopicListView.as_view(), name="topic-list"),
    path("topics/create/", TopicCreateView.as_view(), name="topic-create"),
    path("topics/update/<int:pk>/", TopicUpdateView.as_view(), name="topic-update"),
    path("topics/delete/<int:pk>/", TopicDeleteView.as_view(), name="topic-delete"),

]

app_name = "newspaper"
