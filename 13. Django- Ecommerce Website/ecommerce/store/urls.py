from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('product/<int:pk>', views.product, name='product'),
    path('register/', views.user_register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout', views.user_logout, name='logout'),
    path('new_products', views.new_products, name='new_products'),
    path('sale', views.sale_products, name='sale'),
    path('featured', views.featured_products, name='featured'),
]