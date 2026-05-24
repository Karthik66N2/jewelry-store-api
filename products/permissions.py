from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsAdminOrReadOnly(BasePermission):

    def has_permission(self, request, view):

        # Allow GET requests for everyone
        if request.method in SAFE_METHODS:
            return True

        # Only admins can POST, PUT, DELETE
        return request.user and request.user.is_staff