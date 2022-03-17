from rest_framework import viewsets
from rest_framework import filters
from rest_framework import permissions

from posts.models import Post, Group, Follow
from .serializers import PostSerializer, CommentSerializer, FollowSerializer


class FollowViewSet(ListCreateViewSet):

    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = FollowSerializer
    queryset = Follow.objects.all()
    filter_backends = (filters.SearchFilter,)
    search_fields = ("following__username",)

    def get_queryset(self):
        new_queryset = Follow.objects.filter(user=self.request.user.id)
        return new_queryset

    def perform_create(self, serializer):
        serializer.save(
            user=self.request.user, following=self.context["following"]
        )
