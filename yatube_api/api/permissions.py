from rest_framework import permissions


class OwnerOrReading(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        return (request.user.is_superuser
                or request.method in permissions.SAFE_METHODS
                or obj.author == request.user)
