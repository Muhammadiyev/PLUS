from django.urls import path, include
from django.conf.urls import url
from rest_framework import routers
from .views import (
    GlobalViewSet,
    LocalViewSet,
    LocalViewSetAllFilter,
    GlobalViewSetAllFilter,
)
router = routers.DefaultRouter()

router.register('global', GlobalViewSet)
router.register('local', LocalViewSet)

router.register('all', LocalViewSetAllFilter)
router.register('all', GlobalViewSetAllFilter)


urlpatterns = [
    path('', include(router.urls)),
]
