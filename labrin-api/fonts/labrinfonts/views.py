from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.views import APIView
from .models import FontFamily
from .models import Category
from .models import Font
from .models import User
from .serializers import FontFamilyPostSerializer
from .serializers import FontFamilyDetailSerializer
from .serializers import CategorySerializer
from .serializers import FontDetailSerializer
from .serializers import FontPostSerializer
from . import serializers


class MultiSerializerViewSet(viewsets.ModelViewSet):
    serializers = {
        'default': None,
    }
    def get_serializer_class(self):
        return self.serializers.get(self.action,
                                    self.serializers['default'])


class FontFamilyViewset(MultiSerializerViewSet):
    serializers = {
        "create": FontFamilyPostSerializer,
        "update": FontFamilyPostSerializer,
        "default": FontFamilyDetailSerializer,
        "retrieve": FontFamilyDetailSerializer,
        "list": FontFamilyDetailSerializer,
    }
    queryset = FontFamily.objects.all()

class CategoryViewset(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = serializers.CategorySerializer    

class FontViewset(MultiSerializerViewSet):
    queryset = Font.objects.all()
    serializers = {
        "create": FontPostSerializer,
        "update": FontPostSerializer,
        "default": FontDetailSerializer,
        "retrieve": FontDetailSerializer,
        "list": FontDetailSerializer,
    }    


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer
