from django.urls import path
from . import views

urlpatterns = [
    path('admin_portal', views.admin_portal, name='admin_portal'),
    path('add_product', views.add_product, name='add_product'),
]