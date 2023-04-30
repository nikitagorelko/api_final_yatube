from django.db.models.query import QuerySet
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework.serializers import ModelSerializer
from rest_framework.pagination import LimitOffsetPagination

from api.permissions import IsAuthorOrReadOnly
from api.serializers import CommentSerializer, GroupSerializer, PostSerializer, FollowSerializer
from posts.models import Group, Post, Follow

User = get_user_model()


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (IsAuthorOrReadOnly, IsAuthenticatedOrReadOnly)
    pagination_class = LimitOffsetPagination

    def perform_create(self, serializer: ModelSerializer) -> None:
        serializer.save(author=self.request.user)


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = (IsAuthorOrReadOnly, IsAuthenticatedOrReadOnly)

    def get_post(self) -> Post:
        return get_object_or_404(Post, pk=self.kwargs.get('post_id'))

    def get_queryset(self) -> QuerySet:
        return self.get_post().comments.all()

    def perform_create(self, serializer: ModelSerializer) -> None:
        post = self.get_post()
        serializer.save(author=self.request.user, post=post)


class FollowViewSet(viewsets.ModelViewSet):
    serializer_class = FollowSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self) -> QuerySet:
        user = get_object_or_404(User, pk=self.request.user.pk)
        return user.following.all()

    def perform_create(self, serializer: ModelSerializer) -> None:
        following = get_object_or_404(User, username=self.kwargs.get('following'))
        serializer.save(user=self.request.user, following=following)
