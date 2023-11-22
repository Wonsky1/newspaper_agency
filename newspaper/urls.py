from django.urls import path, include

from newspaper.views import (
    NewspaperListView,
    NewspaperDetailView,
)

urlpatterns = [
    path("", NewspaperListView.as_view(), name="newspaper-list"),
    path("article/<int:pk>/", NewspaperDetailView.as_view(), name="newspaper-detail"),
]

app_name = "newspaper"
