from rest_framework import serializers
from rest_framework.relations import (SlugRelatedField,
                                      StringRelatedField)

from posts.models import Comment, Group, Follow, Post, User


class GroupSerializer(serializers.ModelSerializer):
    """Сериалайзер для модели Group."""

    class Meta:
        fields = ('id', 'title', 'slug', 'description')
        model = Group


class PostSerializer(serializers.ModelSerializer):
    """Сериалайзер для модели Post."""
    author = StringRelatedField(read_only=True)

    class Meta:
        fields = ('id', 'text', 'pub_date', 'author', 'image', 'group')
        model = Post


class CommentSerializer(serializers.ModelSerializer):
    """Сериалайзер для модели Comment."""
    author = serializers.StringRelatedField(read_only=True)
    post = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        fields = ('id', 'author', 'post', 'text', 'created')
        model = Comment


class FollowSerializer(serializers.ModelSerializer):
    """Сериалайзер для модели Follow."""
    user = serializers.SlugRelatedField(
        slug_field='username',
        read_only=True,
        default=serializers.CurrentUserDefault())
    following = SlugRelatedField(
        slug_field='username',
        queryset=User.objects.all())

    class Meta:
        fields = ('user', 'following')
        model = Follow

    def validate(self, data):
        if data['user'] == data['following']:
            raise serializers.ValidationError("Нельзя подписаться на себя")
        return data
