from django.urls import path

from newspaper.views import (
    NewspaperListView,
    NewspaperDetailView,
    RedactorListView,
    RedactorCreateView,
    RedactorUpdateView,
    RedactorDeleteView,
    RedactorDetailView,
    TopicListView,
    TopicCreateView,
    TopicDeleteView,
    TopicUpdateView,
    TopicDetailView,
    NewspaperDeleteView,
    NewspaperCreateView,
    NewspaperUpdateView,

)

urlpatterns = [
    path("", NewspaperListView.as_view(), name="newspaper-list"),
    path(
        "article/<int:pk>/delete/",
        NewspaperDeleteView.as_view(),
        name="newspaper-delete"
    ),
    path(
        "article/<int:pk>/detail",
        NewspaperDetailView.as_view(),
        name="newspaper-detail"
    ),
    path(
        "article/create/",
        NewspaperCreateView.as_view(),
        name="newspaper-create"
    ),
    path(
        "article/<int:pk>/update/",
        NewspaperUpdateView.as_view(),
        name="newspaper-update"
    ),
    path("redactors/", RedactorListView.as_view(), name="redactor-list"),
    path(
        "redactors/<int:pk>/delete/",
        RedactorDeleteView.as_view(),
        name="redactor-delete"
    ),
    path(
        "redactors/create/",
        RedactorCreateView.as_view(),
        name="redactor-create"
    ),
    path(
        "redactors/<int:pk>/update/",
        RedactorUpdateView.as_view(),
        name="redactor-update"
    ),
    path(
        "redactors/<int:pk>/detail/",
        RedactorDetailView.as_view(),
        name="redactor-detail"
    ),
    path("topics/", TopicListView.as_view(), name="topic-list"),
    path("topics/create/", TopicCreateView.as_view(), name="topic-create"),
    path(
        "topics/<int:pk>/update/",
        TopicUpdateView.as_view(),
        name="topic-update"
    ),
    path(
        "topics/<int:pk>/delete/",
        TopicDeleteView.as_view(),
        name="topic-delete"
    ),
    path(
        "topics/<int:pk>/detail/",
        TopicDetailView.as_view(),
        name="topic-detail"
    ),
]

app_name = "newspaper"
