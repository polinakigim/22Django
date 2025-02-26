from django.urls import reverse_lazy
from django.views.generic import (CreateView, DeleteView, DetailView, ListView,
                                  TemplateView, UpdateView)

from django.contrib.auth.mixins import LoginRequiredMixin
from catalog.forms import ProductForm
from catalog.models import Product


class ContactsTemplateView(TemplateView):
    model = Product
    template_name = "catalog/contacts.html"


class ProductListView(ListView):
    model = Product
    template_name = "catalog/product_list.html"


class ProductDetailView(DetailView):
    model = Product


class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy("catalog:product_list")


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy("catalog:product_list")


class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy("catalog:product_list")
