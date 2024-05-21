from django.urls import path, include
from rest_framework import routers

from . import views
from .views import get_csrf_token

router = routers.DefaultRouter()

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('products/', views.ProductListView.as_view(), name='product-list'),
    path('categories/', views.CategoryListView.as_view(), name='category-list'),
    path('register_users/', views.UserCreateView, name='user-register' ),
    path('api/csrf/', get_csrf_token, name='api-csrf-token'),
    
]



