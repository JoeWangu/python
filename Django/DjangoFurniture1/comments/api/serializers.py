from rest_framework.serializers import (
    ModelSerializer,
    SerializerMethodField,
)
from comments.models import Comment


class CommentSerializer(ModelSerializer):
    user = SerializerMethodField()
    class Meta:
        model = Comment
        fields = [
            'id',
            'user',
            'post',
            'name',
            'email',
            'created_on',
            'body',
        ]

    def get_user(self, obj):
        return str(obj.user.username)


    def get_user(self, obj):
        return str(obj.user.username)
