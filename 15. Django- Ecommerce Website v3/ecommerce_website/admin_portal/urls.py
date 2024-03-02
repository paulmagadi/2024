from django.urls import path
from . import views

urlpatterns = [
    path('admin_portal', views.admin_portal, name='admin_portal'),
]