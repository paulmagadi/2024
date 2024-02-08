from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    path('signin/', views.admin_signin, name='signin'),
    path('signout/', views.admin_signout, name='signout'),
    path('signup/', views.admin_signup, name='signup'),
    path('upload/', views.add_product, name='upload'),
    
]