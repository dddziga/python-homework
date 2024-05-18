from django.shortcuts import get_object_or_404
from django.views.generic import ListView, DetailView
from .models import Category, Brand, Key

from django.views.generic import TemplateView

class MainPageView(TemplateView):
    template_name = 'catalog/index.html'


class CategoryListView(ListView):
    model = Category
    template_name = 'catalog/category_list.html'
    context_object_name = 'categories'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        categories = Category.objects.all()
        for category in categories:
            category.brands = Brand.objects.filter(key__category=category).distinct()
            category.keys = Key.objects.filter(category=category)
        context['categories'] = categories
        return context

class BrandListView(ListView):
    model = Brand
    template_name = 'catalog/brand_list.html'
    context_object_name = 'brands'

    def get_queryset(self):
        self.category = get_object_or_404(Category, id=self.kwargs['category_id'])
        return Brand.objects.filter(key__category=self.category).distinct()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = self.category
        return context

class KeyListView(ListView):
    model = Key
    template_name = 'catalog/key_list.html'
    context_object_name = 'keys'

    def get_queryset(self):
        self.category = get_object_or_404(Category, id=self.kwargs['category_id'])
        self.brand = get_object_or_404(Brand, id=self.kwargs['brand_id'])
        return Key.objects.filter(category=self.category, brand=self.brand)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = self.category
        context['brand'] = self.brand
        return context

class KeyDetailView(DetailView):
    model = Key
    template_name = 'catalog/key_detail.html'
    context_object_name = 'key'

    def get_object(self):
        category = get_object_or_404(Category, id=self.kwargs['category_id'])
        brand = get_object_or_404(Brand, id=self.kwargs['brand_id'])
        key = get_object_or_404(Key, id=self.kwargs['key_id'], category=category, brand=brand)
        return key
