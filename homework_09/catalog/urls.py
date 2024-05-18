from django.urls import path
from .views import MainPageView, CategoryListView, BrandListView, KeyListView, KeyDetailView

urlpatterns = [
    path('', MainPageView.as_view(), name='main_page'),
    path('catalog/', CategoryListView.as_view(), name='category_list'),
    path('catalog/<int:category_id>/', BrandListView.as_view(), name='brand_list'),
    path('catalog/<int:category_id>/<int:brand_id>/', KeyListView.as_view(), name='key_list'),
    path('catalog/<int:category_id>/<int:brand_id>/<int:key_id>/', KeyDetailView.as_view(), name='key_detail'),
]
