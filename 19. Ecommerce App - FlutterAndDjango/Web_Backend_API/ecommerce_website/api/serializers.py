from django.contrib.auth.models import User
from store.models import Product, Category, Specification
from api.models import MobileBanner
from rest_framework import serializers

from djoser.serializers import UserCreateSerializer as BaseUserCreateSerializer, UserSerializer as BaseUserSerializer

from django.contrib.auth import get_user_model

User = get_user_model()

class UserCreateSerializer(BaseUserCreateSerializer):
    first_name = serializers.CharField(required=True)
    last_name = serializers.CharField(required=True)

    class Meta(BaseUserCreateSerializer.Meta):
        model = User
        fields = ['id', 'username', 'email', 'password', 'first_name', 'last_name']

    def create(self, validated_data):
        user = super().create(validated_data)
        user.first_name = validated_data['first_name']
        user.last_name = validated_data['last_name']
        user.save()
        return user

class UserSerializer(BaseUserSerializer):
    class Meta(BaseUserSerializer.Meta):
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name']



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

class MobileBannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = MobileBanner
        fields = '__all__'