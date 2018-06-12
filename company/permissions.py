from accounts.permissions import IsSuperAdmin


class IsCompanyOwner(IsSuperAdmin):
    
    def has_object_permission(self, request, view, obj):
        if hasattr(request.user, 'profile') and hasattr(request.user, 'client'):
            profile = request.user.profile
            client = request.user.client
            if profile.is_admin or client.company == obj:
                return True
            
        return super(IsCompanyOwner, self).has_object_permission(request, view, obj)