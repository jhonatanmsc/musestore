from rest_framework import serializers

from apps.core.models import Product, SubCategory


class SubCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = SubCategory
        fields = ['id', 'title']
        read_only_fields = ['id']


class ProductSerializer(serializers.ModelSerializer):
    sub_categories = SubCategorySerializer(many=True)

    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'price', 'image', 'category', 'sub_categories', 'created_at',
                  'updated_at']
        read_only_fields = ['id', 'created_at', 'updated_at']


