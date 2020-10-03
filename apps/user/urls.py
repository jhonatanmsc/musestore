from django.urls import path, include
from rest_framework_jwt.views import refresh_jwt_token

from apps.user.views import UserViewSet, AuthToken
from musestore import drf_router

user_router = drf_router
user_router.register(r'users', UserViewSet)

urlpatterns = [
    path('', include(user_router.urls)),
    path('login/', AuthToken.as_view(), name='obtain-token'),
    path('refresh-token/', refresh_jwt_token, name='refresh-token')
]
