
from django.contrib import admin
from django.urls import path, include

from django.conf.urls.static import static
from . import settings

from django.urls import re_path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView



schema_view = get_schema_view(
   openapi.Info(
      title="Bellamore Backend API",
      default_version='v1',
      description="Backend API",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('store.urls')),
    path('cart/', include('cart.urls')),
    path('', include('core.urls')),
    path('', include('admin_portal.urls')),
    path('payment/', include('payment.urls')),
    path('api/', include('api.urls')),
    path('api/documentation/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
   #  path('auth/', include('djoser.urls')),
   #  path('auth/',  include('djoser.urls.authtoken')),
   #  path('api/', include('djoser.urls')),
   #  path('api/', include('djoser.urls.jwt')),
   #  path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
   #  path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

