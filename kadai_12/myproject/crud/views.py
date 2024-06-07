from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Product
from django.urls import reverse_lazy


class ProductListView(ListView):
    model = Product
    template_name = "list.html"

class ProductCreateView(CreateView):
    model = Product
    # template_name = 'product_form.html'
    fields = '__all__'
    # fields = ['name', 'price']
    success_url = '/crud/'

class ProductUpdateView(UpdateView):
    model = Product
    fields = '__all__'
    template_name_suffix = '_update_form'
    success_url = '/crud/'

class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy('list')

class ProductDetailView(DetailView):
    model = Product
    context_object_name = 'product'
    template_name = 'crud/product_detail.html'
