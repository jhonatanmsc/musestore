import pdb

from django.db import transaction
from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets, status
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

from apps.core.models import Product, Category
from apps.core.serializers import ProductSerializer, CategorySerializer, SlimProductSerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.filter(is_active=True)
    serializer_class = ProductSerializer

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    @transaction.atomic
    def create(self, request, *args, **kwargs):
        serializer = SlimProductSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        category = Category.objects.filter(title=request.data['category']['title'])
        sub_categories = [sub_category['title'] for sub_category in request.data['sub_categories']]
        sub_categories_not = []
        for sub in sub_categories:
            if not Category.objects.filter(title=sub).exists():
                sub_categories_not.append(sub)
        if category.exists():
            if len(sub_categories) > 0 and len(sub_categories_not) > 0:
                return Response({'detail': f'Sub categories {", ".join(sub_categories_not)} does not be exists'},
                                status=status.HTTP_404_NOT_FOUND)
            category = Category.objects.get(title=request.data['category']['title'])
        else:
            Response({'detail': 'Category does not be exists'}, status=status.HTTP_404_NOT_FOUND)
        instance = serializer.save()
        instance.category = category
        for sub in sub_categories:
            instance.sub_categories.add(Category.objects.get(title=sub))
        instance.save()
        return Response(self.serializer_class(instance).data, status=status.HTTP_201_CREATED)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.is_active = False
        instance.save()
        return Response('Product removed.', status=status.HTTP_200_OK)


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.filter(is_sub_category=False)
    serializer_class = CategorySerializer

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    @transaction.atomic
    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        instance = serializer.save()
        instance.is_sub_category = False
        instance.save()
        return Response(serializer.data, status=status.HTTP_200_OK)


class SubCategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.filter(is_sub_category=True)
    serializer_class = CategorySerializer
