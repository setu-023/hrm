from rest_framework.permissions import BasePermission
from rest_framework.exceptions import NotAcceptable, PermissionDenied
import jwt


USER_GROUPS = {
    'superuser': [
        '*'
    ],
    'user': [
        'can_change_password',
        'can_get_own_data'

    ]
}


class UserPermission(BasePermission):
    def __init__(self, permission):
        super(UserPermission, self).__init__()
        self.permission = permission

    def has_permission(self, request, view):
   
            
        if not request.user.groups:
            raise NotAcceptable(detail='group has to be in the user object')
        if '*' in USER_GROUPS.get(request.user.groups[0]):
            return True
        
        # if request.method == 'GET' and request.id!=request.user.id:
        #     return False # not grant access
        # return True # grant access otherwise
  
        if not USER_GROUPS.get(request.user.groups[0]) or self.permission not in USER_GROUPS.get(
            request.user.groups[0],
        ):

            raise PermissionDenied(detail='user has no permission to perform this task')
        return True

class CustomUpdatePermission(BasePermission):
    """
    Permission class to check that a user can update his own resource only
    """
    def __init__(self, permission):
        super(CustomUpdatePermission, self).__init__()
        self.permission = permission

    def has_permission(self, request, view):
        # check that its an update request and user is modifying his resource only
        return view.kwargs['pk']
        if view.kwargs['pk'] != view.user.id:
            return False # not grant access
        return True # grant access otherwise