from rest_framework.permissions import BasePermission


class AddSecurity(BasePermission):
    def has_permission(self, request, view):
        return request.user.has_perm('users.add_secutiry')


class ChangeSecurity(BasePermission):
    def has_permission(self, request, view):
        return request.user.has_perm('users.change_secutiry')


class DeleteSecurity(BasePermission):
    def has_permission(self, request, view):
        return request.user.has_perm('users.delete_security')


class ViewSecurity(BasePermission):
    def has_permission(self, request, view):
        return request.user.has_perm('users.view_security')