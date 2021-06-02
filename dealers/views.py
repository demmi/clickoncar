from django.shortcuts import render
from .models import Dealer
from django.views.generic import ListView, DetailView


class DealersListView(ListView):
    model = Dealer
    template_name = 'dealers_list.html'


class DealersBrandView(ListView):
    model = Dealer
    template_name = 'dealer_brands.html'


class DealerDetailView(DetailView):
    model = Dealer
    template_name = 'dealer.html'

