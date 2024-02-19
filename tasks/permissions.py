from rest_framework.permissions import BasePermission, SAFE_METHODS

class IsTaskOwner(BasePermission):
    """
    Allows modify access only to owner.
    """

    

    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        return False

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        return obj.user == request.user


