from rest_framework import permissions


class IsOwnerOrAdminOrUser(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.user.is_staff or request.user.is_superuser:
            return True
        elif request.user == obj.whose:
            return True
        return request.user == obj.owner
