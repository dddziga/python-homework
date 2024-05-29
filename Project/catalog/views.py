from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView, TemplateView
from .models import Category, Brand, Key, Cart, CartItem, Order, OrderItem

@login_required
def create_order(request):
    cart = get_object_or_404(Cart, user=request.user)
    order = Order.objects.create(user=request.user)
    cart_items = CartItem.objects.filter(cart=cart)
    for item in cart_items:
        OrderItem.objects.create(order=order, key=item.key, quantity=item.quantity)
    cart_items.delete()
    return redirect('order_detail', order_id=order.id)

@login_required
def order_detail(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    items = OrderItem.objects.filter(order=order)
    return render(request, 'catalog/order_detail.html', {'order': order, 'items': items})

@login_required
def confirm_order(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    order.is_confirmed = True
    order.save()
    return redirect('order_detail', order_id=order.id)

@login_required
def add_to_cart(request, key_id):
    key = get_object_or_404(Key, id=key_id)
    cart, created = Cart.objects.get_or_create(user=request.user)
    cart_item, created = CartItem.objects.get_or_create(cart=cart, key=key)
    cart_item.quantity += 1
    cart_item.save()
    return redirect('cart_detail')

@login_required
def remove_from_cart(request, item_id):
    cart_item = get_object_or_404(CartItem, id=item_id)
    cart_item.delete()
    return redirect('cart_detail')

@login_required
def cart_detail(request):
    cart, created = Cart.objects.get_or_create(user=request.user)
    items = CartItem.objects.filter(cart=cart)
    return render(request, 'catalog/cart_detail.html', {'cart': cart, 'items': items})

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
