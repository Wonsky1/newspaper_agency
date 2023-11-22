from django.shortcuts import render
from django.views import generic

from newspaper.models import Newspaper, Redactor, Topic


class NewspaperListView(generic.ListView):
    model = Newspaper
    queryset = Newspaper.objects.select_related("topic")
    paginate_by = 6


class NewspaperDetailView(generic.DetailView):
    model = Newspaper


class RedactorListView(generic.ListView):
    model = Redactor
    paginate_by = 10


class TopicListView(generic.ListView):
    model = Topic

