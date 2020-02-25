from rest_framework import serializers
from .models import FontFamily
from .models import Font
from .models import User
from .models import Category
from rest_auth.serializers import LoginSerializer as RestAuthLoginSerializer


class LoginSerializer(RestAuthLoginSerializer):
    username = None


class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Category
        fields = ("id","name")

class FontFamilyDetailSerializer(serializers.HyperlinkedModelSerializer):
    category = CategorySerializer(read_only = True)
    class Meta:
        model = FontFamily
        fields = ("id","name","description","category")


class FontFamilyPostSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = FontFamily
        fields = ("id","name","description","category")


class FontDetailSerializer(serializers.HyperlinkedModelSerializer):
    family = FontFamilyDetailSerializer(read_only = True)
    class Meta:
        model = Font
        fields = ('id','name','font_file', 'family')

class FontPostSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Font
        fields = ('id','name','font_file', 'family')

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('email', 'full_name', )