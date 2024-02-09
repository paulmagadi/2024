from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('product/<int:pk>', views.product, name='product'),
    path('category/<str:f>', views.category, name='category'),
    path('categories/', views.all_categories, name='categories'),
    path('login', views.user_login, name='login'),
    path('logout', views.user_logout, name='logout'),
    path('register', views.register_user, name='register'),
    path('sale/', views.on_sale, name='sale'),
    path('new/', views.new_product, name='new'),
    path('featured/', views.featured, name='featured'),
    
]
