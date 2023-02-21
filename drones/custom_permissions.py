from rest_framework import permissions


class IsCurrentUserOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            # the method is a safe method
            return True
        # if method is not in safe methods
        # only owners are granted permissions to unsafe methods
        return obj.owner == request.user
