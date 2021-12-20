from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, DetailView, ListView

from categoryapp.form import CategoryCreationForm
from categoryapp.models import Categorylist


class CategoryCreateView(CreateView):
    model = Categorylist
    form_class = CategoryCreationForm
    success_url = reverse_lazy('vocapp:create')
    template_name = 'category/create.html'

    def get_success_url(self):
        return reverse('categoryapp:list')

class CategoryListView(ListView):
    model= Categorylist
    context_object_name = 'categorylist'
    template_name = 'category/category_list.html'
    paginate_by = 25







