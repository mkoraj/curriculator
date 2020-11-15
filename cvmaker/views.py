from django.http import request
from django.shortcuts import render
from django.views import View

from django.urls import reverse, reverse_lazy

from django.views.generic.base import TemplateView
from django.views.generic import CreateView, ListView, DetailView
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse

from . import forms, models

class IndexView(TemplateView):
    template_name = 'index.html'

class PersonListView(ListView):

    model = models.Person
    template_name = "person_list.html"
    paginate_by = 100 # if pagination is desired

    def get_queryset(self):
        return self.model.objects.all()

class PersonCreateView(CreateView):
    model = models.Person
    form_class = forms.CreatePersonForm
    template_name = "person_create.html"
    success_url = reverse_lazy('IndexView')
    success_message = "Person with id '{id}' was created successfully"

    def get_success_url(self):
        person = self.object
        return reverse_lazy('cvmaker:person_list')
        # return reverse_lazy('index', args=[person.pk])

    def get_success_message(self, cleaned_data):
        return self.success_message.format(id=self.object.id)

    # def form_valid(self, form):
    #     person = form.save(commit=False)
    #     person.created_by = self.request.user
    #     person.save()

    #     return super().form_valid(form)

class PersonDetailView(DetailView):

    template_name = "person_detail.html"
    model = models.Person

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
