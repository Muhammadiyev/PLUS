from django.urls import path, include
from django.conf.urls import url
from rest_framework import routers
from .views import (
    UserViewSet,
)
router = routers.DefaultRouter()

router.register('users', UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
