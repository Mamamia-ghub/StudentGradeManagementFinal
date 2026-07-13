from rest_framework import permissions

class IsTeacherOrStudentOwner(permissions.BasePermission):
    """
    Custom isolation rule:
    - Teachers maintain full CRUD permissions on items.
    - Students are locked into read-only access for records that belong directly to them.
    """
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role in ['ADMIN', 'TEACHER', 'STUDENT']

    def has_object_permission(self, request, view, obj):
        if request.user.role == 'ADMIN':
            return True
            
        if request.user.is_teacher():
            return True

        if request.user.is_student():
            if obj.__class__.__name__ == 'User':
                return obj == request.user
                
            if hasattr(obj, 'enrollment'):
                return obj.enrollment.student == request.user
                
            if hasattr(obj, 'student'):
                return obj.student == request.user
                
        return False

