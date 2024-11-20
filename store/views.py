from django.shortcuts import render, get_object_or_404

from django.views.generic import ListView, DetailView
from store.utils import DataMixin
from .models import Products

class MainPage(DataMixin, ListView):
    template_name = 'index.html'
    title_page = 'My Shop'
    queryset = Products.objects.all()
    context_object_name = 'posts'

class ProductPage(DataMixin, DetailView): #переделать в DetailView когда появятся Слаги в БД
    template_name = 'product.html'
    title_page = 'Detail Information'
    context_object_name = 'post'
    queryset = Products.objects.all()
    id_url_kwarg = 'id'

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     return self.get_mixin_context(context, title_product=context['post'].title)

    def get_object(self, queryset=None):
        return get_object_or_404(Products.objects, id=self.kwargs[self.id_url_kwarg])



class BasketPage(DataMixin, ListView):
    template_name = 'basket.html'
    title_page = 'Shopping Cart'
    queryset = Products.objects.all()

