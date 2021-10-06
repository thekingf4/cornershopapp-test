from rest_framework.permissions import BasePermission


class IsAccountOwner(BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.user == obj


class AddUser(BasePermission):
    def has_permission(self, request, view):
        return request.user.has_perm('users.add_user')


class ChangeUser(BasePermission):
    def has_permission(self, request, view):
        return request.user.has_perm('users.change_user')


class DeleteUser(BasePermission):
    def has_permission(self, request, view):
        return request.user.has_perm('users.delete_user')


class ViewUser(BasePermission):
    def has_permission(self, request, view):
        return request.user.has_perm('users.view_user')


class AcceptUser(BasePermission):
    def has_permission(self, request, view):
        return request.user.has_perm('users.can_accept_user')


class ListUser(BasePermission):
    def has_permission(self, request, view):
        return request.user.has_perm('users.can_list_user')