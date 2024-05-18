from django.contrib.auth.models import Group, User
from store.models import Product, Category, Specification
from api.models import MobileBanner
from rest_framework import serializers

from djoser.serializers import UserCreateSerializer
from rest_framework import serializers
from store.models import UserProfile

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['first_name', 'last_name']

class UserSerializer(serializers.ModelSerializer):
    profile = UserProfileSerializer()
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'profile', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        profile_data = validated_data.pop('profile')
        user = User.objects.create_user(**validated_data)
        UserProfile.objects.create(user=user, **profile_data)
        return user


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