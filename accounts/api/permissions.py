from rest_framework import permissions


class IsAdmin(permissions.IsAdminUser):

    """
    Custom permission for admin
    """

    def has_permission(self, request, view):
        if hasattr(request.user, 'profile'):
            profile = request.user.profile
            if profile.is_admin:
                return True

        return super(IsAdmin, self).has_permission(request, view)


class IsClientOrAdmin(IsAdmin):

    """
    Custom permission for clients
    """

    def has_permission(self, request, view):
        if hasattr(request.user, 'client') and hasattr(request.user, 'profile'):
            return True

        return super(IsClientOrAdmin, self).has_permission(request, view)


class IsManagerOrAdmin(IsAdmin):
    """
    Custom permission for managers
    """
    def has_permission(self, request, view):
        if hasattr(request.user, 'client') and hasattr(request.user, 'profile'):
            profile = request.user.profile
            if profile.is_manager:
                return True

        return super(IsManagerOrAdmin, self).has_permission(request, view)


class IsManagerClientOrAdmin(IsAdmin):

    def has_permission(self, request, view):

        if hasattr(request.user, 'profile'):
            profile = request.user.profile
            if profile.is_manager or hasattr(request.user, 'client'):
                return True

        return super(IsManagerClientOrAdmin, self).has_permission(request, view)

# Object level permissions


class IsSuperAdmin(permissions.BasePermission):
    # SuperAdmin can create/update/list/destroy everything
    def has_object_permission(self, request, view, obj):

        if request.user.is_superuser:
            return True

        return False


class IsUserOwner(IsSuperAdmin):

    def has_object_permission(self, request, view, obj):
        if hasattr(request.user, 'profile'):
            profile = request.user.profile
            if obj == request.user or profile.is_admin:
                return True

        return super(IsUserOwner, self).has_object_permission(request, view, obj)


class IsProfileOwner(IsSuperAdmin):

    def has_object_permission(self, request, view, obj):

        if hasattr(request.user, 'profile'):
            profile = request.user.profile

            if obj == profile or profile.is_admin:
                return True

        return super(IsProfileOwner, self).has_object_permission(request, view, obj)


class IsClientOwner(IsSuperAdmin):

    def has_object_permission(self, request, view, obj):

        if hasattr(request.user, 'client') and hasattr(request.user, 'profile'):
            client = request.user.client
            profile = request.user.profile

            if obj == client or profile.is_admin:
                return True
        
        return super(IsClientOwner, self).has_object_permission(request, view, obj)

