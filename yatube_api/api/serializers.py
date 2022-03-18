from rest_framework import serializers
from rest_framework.relations import SlugRelatedField
from rest_framework.validators import UniqueTogetherValidator

from posts.models import Comment, Follow, Group, Post, User


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ("title",)


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        read_only=True, slug_field="username"
    )

    class Meta:
        fields = "__all__"
        model = Comment


class PostSerializer(serializers.ModelSerializer):
    group = serializers.PrimaryKeyRelatedField(
        queryset=Group.objects.all(), required=False
    )
    comment = CommentSerializer(many=True, required=False)
    author = serializers.StringRelatedField(read_only=True)

    class Meta:
        fields = (
            "id",
            "text",
            "author",
            "image",
            "pub_date",
            "group",
            "comment",
        )
        model = Post


class FollowSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(
        slug_field="username",
        read_only=True,
        default=serializers.CurrentUserDefault(),
    )

    following = serializers.SlugRelatedField(
        slug_field="username", queryset=User.objects.all(), required=True
    )

    def validate(self, data):
        if self.context["request"].user == data["following"]:
            raise serializers.ValidationError("Нельзя подписаться на себя")
        return data

    class Meta:
        fields = ("user", "following")
        model = Follow
        validators = [
            UniqueTogetherValidator(
                queryset=Follow.objects.all(), fields=("user", "following")
            )
        ]
