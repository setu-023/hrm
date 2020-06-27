from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, CreateAPIView
from rest_framework import permissions, status
from rest_framework.response import Response

from department.models import Department
from department.serializers import DepartmentSerializer
from department.permission import UserPermission



class DepartmentListCreateAPIView(ListCreateAPIView):
    serializer_class = DepartmentSerializer
    queryset = Department.objects.filter()

    def get_permissions(self):
        if self.request.method == 'POST':
            return (UserPermission('can_get_users'),)

        elif self.request.method == 'GET':
            return (permissions.AllowAny(),)
        raise MethodNotAllowed(method=self.request.method)
    
    
    
    def get(self, request, format=None):
        """
        Return a list of all users.
        """
        dept        = Department.objects.all()
        
        # dept        = [dept.name for dept in Department.objects.all()]
        serializer  = DepartmentSerializer(dept, many=True)

        return Response({'data':serializer.data}, status.HTTP_200_OK,)