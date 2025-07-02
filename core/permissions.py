from rest_framework.permissions import BasePermission


class IsPonOwnerPermission(BasePermission):
    def has_object_permission(self, request, view, obj):
        user = request.user
        return user == obj.owner
    

class IsBoardOwner(BasePermission):
    def has_object_permission(self, request, view, obj):
        user = request.user
        return user == obj.owner