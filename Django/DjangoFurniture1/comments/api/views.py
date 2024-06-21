from rest_framework.generics import (
    # CreateAPIView,
    ListAPIView,
    RetrieveAPIView,
#     RetrieveUpdateAPIView,
#     DestroyAPIView,
)
from comments.models import Comment
from .serializers import (
    CommentSerializer,
    # CommentDetailSerializer,
)
# from rest_framework.permissions import (
#     IsAuthenticated,
#     IsAuthenticatedOrReadOnly,
# )
# from posts.api.permissions import isOwnerOrReadOnly
from django.db.models import Q
from rest_framework.filters import (
    SearchFilter,
    OrderingFilter,
)
# from .pagination import PostLimitOffsetPagination
from posts.api.pagination import PostPageNumberPagination


class CommentListAPIView(ListAPIView):
    serializer_class = CommentSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['content', 'user__first_name']
    pagination_class = PostPageNumberPagination

    def get_queryset(self, *args, **kwargs):
        queryset_list = Comment.objects.all()
        query = self.request.GET.get('q')
        if query:
            queryset_list = queryset_list.filter(
                Q(content__icontains=query) |
                Q(user__first_name__icontains=query) |
                Q(user__last_name__icontains=query)
            ).distinct()
        return queryset_list


class CommentDetailAPIView(RetrieveAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


# class PostUpdateAPIView(RetrieveUpdateAPIView):
#     queryset = Comment.objects.all()
#     serializer_class = CommentSerializer
#     permission_classes = [IsAuthenticatedOrReadOnly, isOwnerOrReadOnly]

#     def perform_update(self, serializer):
#         serializer.save(user=self.request.user)
#         return super().perform_update(serializer)


# class PostDeleteAPIView(DestroyAPIView):
#     queryset = Comment.objects.all()
#     serializer_class = CommentSerializer
#     permission_classes = [IsAuthenticatedOrReadOnly, isOwnerOrReadOnly]


# class PostCreateAPIView(CreateAPIView):
#     queryset = Comment.objects.all()
#     serializer_class = CommentSerializer

#     permission_classes = [IsAuthenticated]

#     def perform_create(self, serializer):
#         serializer.save(user=self.request.user)
#         return super().perform_create(serializer)
