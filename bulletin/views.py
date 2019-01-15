from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from .models import Bulletin

# Create your views here.


class BulletinListView(ListView):
    model = Bulletin
    ordering = "id"
    context_object_name = "bulletins"
    paginate_by = 10


class BulletinDetailView(DetailView):
    model = Bulletin
    context_object_name = "bulletin"
