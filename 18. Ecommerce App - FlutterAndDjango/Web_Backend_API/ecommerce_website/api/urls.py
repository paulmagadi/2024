from django.urls import include, path
from rest_framework import routers

from . import views
# from .views import get_csrf_token

router = routers.DefaultRouter()


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('products/', views.ProductListView.as_view(), name='product-list'),
    path('categories/', views.CategoryListView.as_view(), name='category-list'),
    path('mobile_banner/', views.MobileBannerListView.as_view(), name='mobile-banner-list'),
    path('login/', views.login, name=('login')),
    path('register/', views.register, name=('register')),
    path('logout/', views.logout_user, name='logout'),
#     path('api/csrf/', get_csrf_token, name='api-csrf-token'),
]







