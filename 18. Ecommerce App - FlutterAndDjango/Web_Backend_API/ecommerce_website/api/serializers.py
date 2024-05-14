from django.contrib.auth.models import Group, User
from store.models import Product, Category, Specification
from api.models import MobileBanner
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']
        

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
        
class SpecificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Specification
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    # specification = SpecificationSerializer()
    class Meta:
        model = Product
        fields = '__all__'


class MobileBannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = MobileBanner
        fields = '__all__'