from rest_framework import permissions

class IsCreatorOrStaff(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.is_staff:
            return True
        return request.user == view.get_object().creator

    def has_object_permission(self, request, view, obj):
        # Разрешить только чтение для неавторизованных пользователей
        if request.method in permissions.SAFE_METHODS:
            return True

        # Разрешить изменение или удаление только владельцу привычки
        return obj.creator == request.user