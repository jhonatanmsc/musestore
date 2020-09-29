from django.urls import path, include

from apps.core.views import ProductViewSet
from musestore import drf_router

core_router = drf_router
core_router.register(r'products', ProductViewSet)

urlpatterns = [
    path('', include(core_router.urls))
]