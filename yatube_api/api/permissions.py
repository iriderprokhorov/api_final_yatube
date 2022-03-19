from rest_framework import permissions


class AuthorPermission(permissions.BasePermission):
    """Пермишен для автор"""

    def has_object_permission(self, request, view, obj):
        return (
            request.method in permissions.SAFE_METHODS
            or obj.author == request.user
        )


class FollowPermission(permissions.BasePermission):
    """Пермишен для подписки"""

    def has_object_permission(self, request, view, obj):
        return (
            request.method in permissions.SAFE_METHODS
            or obj.author == request.user
        )
