from pyexpat import model
from rest_framework.serializers import HyperlinkedModelSerializer, ModelSerializer

from ..users.serializers import ShortUserModelSerializer, UserModelSerializer
from .models import Project, Todo


class ShortProjectModelSerializer(ModelSerializer):
    class Meta:
        model = Project
        fields = ("name",)


class ProjectModelSerializer(HyperlinkedModelSerializer):
    user = ShortUserModelSerializer(many=True)

    class Meta:
        model = Project
        fields = "__all__"


class TodoModelSerializer(HyperlinkedModelSerializer):
    project = ShortProjectModelSerializer()
    user = ShortUserModelSerializer()

    class Meta:
        model = Todo
        fields = "__all__"
