from django.shortcuts import render
from .models import Dealer
from catalog.models import Brand
from django.views.generic import ListView, DetailView


class DealersBrandView(ListView):
    model = Brand
    template_name = 'dealer_brands.html'


class DealersListView(ListView):
    model = Dealer
    template_name = 'dealers_list.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        print(self.kwargs['slug'])
        context = super().get_context_data(**kwargs)
        context['dealers_list'] = Dealer.objects.filter(brand__slug=self.kwargs['slug'])
        return context


class DealerDetailView(DetailView):
    model = Dealer
    template_name = 'dealer.html'

