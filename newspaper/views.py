from django.shortcuts import render
from django.views import generic

from newspaper.models import Newspaper


class NewspaperListView(generic.ListView):
    model = Newspaper
    queryset = Newspaper.objects.select_related("topic")
    paginate_by = 6


class NewspaperDetailView(generic.DetailView):
    model = Newspaper
