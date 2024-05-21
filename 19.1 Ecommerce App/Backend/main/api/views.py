from pyexpat.errors import messages
from django.contrib.auth.models import Group, User
from django.shortcuts import redirect, render
from rest_framework import permissions, viewsets, generics
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

from .serializers import ProductSerializer, SpecificationSerializer, CategorySerializer

from store.models import Product, Category
# from .models import MobileBanner


from django.http import JsonResponse
from django.middleware.csrf import get_token

def get_csrf_token(request):
    return JsonResponse({'csrfToken': get_token(request)})


class ProductListView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.AllowAny] 


class CategoryListView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.AllowAny] 

# class MobileBannerListView(generics.ListAPIView):
#     queryset = MobileBanner.objects.all()
#     serializer_class = MobileBannerSerializer
#     permission_classes = [permissions.AllowAny] 