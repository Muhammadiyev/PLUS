from django.shortcuts import render, redirect
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Global, Lacal
from .serializers import GlobalSerializers, LacalSerializers

from rest_framework import generics
from rest_framework import viewsets
from django_filters import rest_framework as filters
from rest_framework.filters import SearchFilter, OrderingFilter


class GlobalViewSet(viewsets.ModelViewSet):
    queryset = Global.objects.all()
    serializer_class = GlobalSerializers

class LocalViewSet(viewsets.ModelViewSet):
    queryset = Lacal.objects.all()
    serializer_class = LacalSerializers