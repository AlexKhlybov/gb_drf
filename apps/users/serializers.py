from ast import Mod

from pyexpat import model
from rest_framework.serializers import HyperlinkedModelSerializer, ModelSerializer

from .models import User


class ShortUserModelSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ("first_name", "last_name")


class UserModelSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = (
            "url",
            "username",
            "first_name",
            "last_name",
            "role",
            "date_joined",
            "is_staff",
            "is_active",
        )
