from django.shortcuts import render, redirect
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Global, Local
from .serializers import GlobalSerializers, LacalSerializers, GlobalSerializersAll, LacalSerializersAll

from rest_framework import generics
from rest_framework import viewsets
from django_filters import rest_framework as filters
from rest_framework.filters import SearchFilter, OrderingFilter


class GlobalViewSet(viewsets.ModelViewSet):
    queryset = Global.objects.all()
    serializer_class = GlobalSerializers

class LocalViewSet(viewsets.ModelViewSet):
    queryset = Local.objects.all()
    serializer_class = LacalSerializers


class LocalViewSetAllFilter(viewsets.ModelViewSet):
    queryset = Local.objects.all()
    serializer_class = LacalSerializersAll
    filter_backends = (filters.DjangoFilterBackend, SearchFilter, OrderingFilter)
    filter_fields = ['local_user']

class GlobalViewSetAllFilter(viewsets.ModelViewSet):
    queryset = Global.objects.all()
    serializer_class = GlobalSerializersAll
    filter_backends = (filters.DjangoFilterBackend, SearchFilter, OrderingFilter)
    filter_fields = ['global_user']