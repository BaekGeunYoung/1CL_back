from rest_framework import permissions


class IsMaster(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.master == request.user