from rest_framework import permissions


class IsModerator(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.groups.filter(name='Модераторы').exists()


class IsOwner(permissions.BasePermission):
    """Проверка, является ли пользователь владельцем урока/курса"""

    def has_object_permission(self, request, view, obj):
        """Проверка прав пользователя на конкретный объект"""
        return request.user == obj.owner
