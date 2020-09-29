from rest_framework import serializers

from apps.core.models import Product, Category


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'title']
        read_only_fields = ['id']


class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    sub_categories = CategorySerializer(many=True)

    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'price', 'image', 'category', 'sub_categories', 'created_at',
                  'updated_at']
        read_only_fields = ['id', 'created_at', 'updated_at']


