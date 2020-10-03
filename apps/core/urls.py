from django.urls import path, include

from apps.core.views import ProductViewSet, CategoryViewSet, SubCategoryViewSet
from musestore import drf_router

core_router = drf_router
core_router.register(r'products', ProductViewSet)
core_router.register(r'categories', CategoryViewSet)
core_router.register(r'sub-category', SubCategoryViewSet)

urlpatterns = [
    path('', include(core_router.urls))
]
