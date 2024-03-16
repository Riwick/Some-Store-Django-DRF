from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsSuperUserOrStaffOrReadOnly(BasePermission):
    def has_object_permission(self, request, view, obj):
        return bool(request.method in SAFE_METHODS
                    or request.user.is_superuser
                    or request.user.is_staff)