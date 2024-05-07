from django.urls import path
from . import views

urlpatterns = [
    path('products/', views.ProductListView.as_view(), name='product-list'),
    path('categories/', views.CategoryListView.as_view(), name='category-list'),
]
