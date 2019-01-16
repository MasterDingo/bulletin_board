from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.db.models import F

from count_views.views import CountableViewMixin

from .models import Bulletin


# Create your views here.


class BulletinListView(ListView):
    model = Bulletin
    ordering = "id"
    context_object_name = "bulletins"
    paginate_by = 10


class BulletinDetailView(CountableViewMixin,DetailView):
    model = Bulletin
    context_object_name = "bulletin"
