from djoser.serializers import UserCreateSerializer, UserSerializer
from rest_framework import serializers
from users.models import CustomUser
from store.models import Product, Category, Specification

class CustomUserCreateSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        model = CustomUser
        fields = ('id', 'email', 'first_name', 'last_name', 'password')

class CustomUserSerializer(UserSerializer):
    class Meta(UserSerializer.Meta):
        model = CustomUser
        fields = ('id', 'email', 'first_name', 'last_name')
    

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
        
class SpecificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Specification
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
        depth = 1

# class MobileBannerSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = MobileBanner
#         fields = '__all__'

