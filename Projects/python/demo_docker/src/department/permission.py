from rest_framework.permissions import BasePermission
from rest_framework.exceptions import NotAcceptable, PermissionDenied


USER_GROUPS = {
    'superuser': [
  
        '*'
    ],
        'user': [

        'can_get_dept'
    ]
}


class UserPermission(BasePermission):
    def __init__(self, permission):
        super(UserPermission, self).__init__()
        self.permission = permission

    def has_permission(self, request, view):
        if not request.headers.get('group'):
            raise NotAcceptable(detail='group has to be in the header')

        if '*' in USER_GROUPS.get(request.user.groups[0]):
            return True
       

        if not USER_GROUPS.get(request.headers['group']) or self.permission not in USER_GROUPS.get(
            request.headers['group']
        ):
            raise PermissionDenied(detail='user has no permission to perform this task')
        return True