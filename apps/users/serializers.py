from rest_framework.serializers import HyperlinkedModelSerializer

from .models import User


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
