from rest_framework.serializers import (
    ModelSerializer,
    HyperlinkedIdentityField,
    SerializerMethodField,
)
from posts.models import Post


class PostListSerializer(ModelSerializer):
    url = HyperlinkedIdentityField(
        view_name='posts-api:detail',
    )
    # delete_url = HyperlinkedIdentityField(
    #     view_name='posts-api:delete',
    #     # lookup_field = 'slug'
    # )
    user = SerializerMethodField()
    class Meta:
        model = Post
        fields = [
            'url',
            'user',
            'id',
            'title',
            'content',
            'publish',
            # 'delete_url',
        ]
        # extra_kwargs = {
        #     'url': {'view_name': 'posts-api:detail', 'lookup_field': 'slug'},
        # }
    def get_user(self, obj):
        return str(obj.user.username)


class PostDetailSerializer(ModelSerializer):
    user = SerializerMethodField()
    image = SerializerMethodField()
    class Meta:
        model = Post
        fields = [
            'id',
            'user',
            'image',
            'title',
            'slug',
            'content',
            'publish',
        ]

    def get_user(self, obj):
        return str(obj.user.username)

    def get_image(self, obj):
        try:
            image = obj.image.url  # obj.image.path
        except:
            image = None
        return image


class PostCreateSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = [
            'image',
            'title',
            'content',
            'publish',
        ]