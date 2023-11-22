from django.urls import path, include

from newspaper.views import (
    NewspaperListView,
    NewspaperDetailView,
    RedactorListView,
    TopicListView,
    TopicCreateView,
    TopicDeleteView,
    TopicUpdateView,
    RedactorDeleteView,
    NewspaperDeleteView,
)

urlpatterns = [
    path("", NewspaperListView.as_view(), name="newspaper-list"),
    path("newspaper/<int:pk>/delete/", NewspaperDeleteView.as_view(), name="newspaper-delete"),
    path("article/<int:pk>/", NewspaperDetailView.as_view(), name="newspaper-detail"),
    path("redactors/", RedactorListView.as_view(), name="redactor-list"),
    path("redactors/delete/<int:pk>/", RedactorDeleteView.as_view(), name="redactor-delete"),
    path("topics/", TopicListView.as_view(), name="topic-list"),
    path("topics/create/", TopicCreateView.as_view(), name="topic-create"),
    path("topics/update/<int:pk>/", TopicUpdateView.as_view(), name="topic-update"),
    path("topics/delete/<int:pk>/", TopicDeleteView.as_view(), name="topic-delete"),

]

app_name = "newspaper"
