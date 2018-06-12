from rest_framework import permissions


class IsAddressOwnerOrAdmin(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object to edit it.
    """

    def has_object_permission(self, request, view, obj):
        # is super admin
        if request.user.is_superuser:
            return True
        # or is object owner
        if hasattr(request.user, 'profile'):
            profile = request.user.profile
            if hasattr(obj, 'profile'):

                if obj.profile == profile or profile.is_admin:
                    return True
                else:
                    return False
            else:
                return False

        return False
