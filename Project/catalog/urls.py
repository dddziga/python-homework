from django.urls import path
from .views import MainPageView, CategoryListView, BrandListView, KeyListView, KeyDetailView, add_to_cart, remove_from_cart, cart_detail, create_order, order_detail, confirm_order

urlpatterns = [
    path('', MainPageView.as_view(), name='main_page'),
    path('catalog/', CategoryListView.as_view(), name='category_list'),
    path('catalog/<int:category_id>/', BrandListView.as_view(), name='brand_list'),
    path('catalog/<int:category_id>/<int:brand_id>/', KeyListView.as_view(), name='key_list'),
    path('catalog/<int:category_id>/<int:brand_id>/<int:key_id>/', KeyDetailView.as_view(), name='key_detail'),
    path('cart/', cart_detail, name='cart_detail'),
    path('cart/add/<int:key_id>/', add_to_cart, name='add_to_cart'),
    path('cart/remove/<int:item_id>/', remove_from_cart, name='remove_from_cart'),
    path('order/create/', create_order, name='create_order'),
    path('order/<int:order_id>/', order_detail, name='order_detail'),
    path('order/<int:order_id>/confirm/', confirm_order, name='confirm_order'),
]