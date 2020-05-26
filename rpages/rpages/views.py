from django.shortcuts import render
from django.views.generic import ListView

from .models import Event


# Create your views here.
class EventListView(ListView):
    model = Event
    context_object_name = 'event_list'
    template_name = 'home.html'

class EventListViewD1(ListView):
    model = Event
    context_object_name = 'event_list'
    template_name = 'D1.html'
    ordering = ['days1']


class EventListViewD2(ListView):
    model = Event
    context_object_name = 'event_list'
    template_name = 'D2.html'
    ordering = ['days2']
