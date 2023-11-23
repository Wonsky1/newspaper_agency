from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views import generic

from newspaper.forms import RedactorCreationForm, NewspaperForm, RedactorUpdateForm
from newspaper.models import Newspaper, Redactor, Topic


class NewspaperListView(generic.ListView):
    model = Newspaper
    queryset = Newspaper.objects.select_related("topic")
    paginate_by = 6


class NewspaperDetailView(LoginRequiredMixin, generic.DetailView):
    model = Newspaper


class NewspaperDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Newspaper


class NewspaperCreateView(LoginRequiredMixin, generic.CreateView):
    model = Newspaper
    form_class = NewspaperForm
    success_url = reverse_lazy("newspaper:newspaper-list")


class NewspaperUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Newspaper
    form_class = NewspaperForm
    success_url = reverse_lazy("newspaper:newspaper-list")


class RedactorListView(generic.ListView):
    model = Redactor
    paginate_by = 10


class RedactorDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Redactor
    success_url = reverse_lazy("newspaper:redactor-list")


class RedactorCreateView(generic.CreateView):
    model = Redactor
    form_class = RedactorCreationForm
    success_url = reverse_lazy("newspaper:redactor-list")


class RedactorUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Redactor
    form_class = RedactorUpdateForm
    success_url = reverse_lazy("newspaper:redactor-list")


class RedactorDetailView(LoginRequiredMixin, generic.DetailView):
    model = Redactor


class TopicListView(generic.ListView):
    model = Topic


class TopicCreateView(LoginRequiredMixin, generic.CreateView):
    model = Topic
    fields = "__all__"
    success_url = reverse_lazy("newspaper:topic-list")


class TopicUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Topic
    fields = "__all__"
    success_url = reverse_lazy("newspaper:topic-list")


class TopicDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Topic
    success_url = reverse_lazy("newspaper:topic-list")


class TopicDetailView(LoginRequiredMixin, generic.DetailView):
    model = Topic


