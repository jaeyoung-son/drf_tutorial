from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    커스텀 권한 오너만 수정가능
    """
    
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        
        return obj.owner == request.user