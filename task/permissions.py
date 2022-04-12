from rest_framework.permissions import BasePermission
from rest_framework import permissions

from rest_framework.permissions import BasePermission
from rest_framework import permissions


class IsUserTaskPermission(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method == 'DELETE':
            return request.user.is_superuser
        else:
            if request.method in permissions.SAFE_METHODS or request.user.is_superuser:
                return True
            return request.user == obj
