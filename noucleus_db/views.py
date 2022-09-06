from django.shortcuts import render
from .models import Gene, Guide, User
from .serializers import GeneSerializer, GuideSerializer, UserSerializer
from rest_framework import generics
# Create your views here.


class GeneList(generics.ListCreateAPIView):
    queryset = Gene.objects.all()
    serializer_class = GeneSerializer


class GeneDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Gene.objects.all()
    serializer_class = GeneSerializer


class GuideList(generics.ListCreateAPIView):
    queryset = Guide.objects.all()
    serializer_class = GuideSerializer


class GuideDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Guide.objects.all()
    serializer_class = GuideSerializer


class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
