from rest_framework.permissions import BasePermission
from rest_framework import permissions

from rest_framework.permissions import BasePermission
from rest_framework import permissions


class IsUserTaskPermission(BasePermission):
    def has_object_permission(self, request, view, obj):
        
        return request.user == obj.user
