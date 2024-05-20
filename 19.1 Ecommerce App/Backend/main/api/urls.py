from django.urls import path, include

urlpatterns = [
    path('auth/', include('djoser.urls')),
    path('auth/token/', include('djoser.urls.authtoken')),  
]