from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('product/<int:pk>', views.product, name='product'),
    path('category/', views.category, name='category'),
    path('sale/', views.sale, name='sale'),
    path('new/', views.new, name='new'),
    path('featured/', views.featured, name='featured'),
    path('offers/', views.offers, name='offers'),
    path('admin_dashboard', views.admin_dashboard, name='admin_dashboard'),
]