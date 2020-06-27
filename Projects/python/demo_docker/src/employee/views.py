from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, CreateAPIView
from rest_framework import permissions, status
from rest_framework.response import Response

from employee.models import Employee
from employee.api.serializers import EmployeeSerializer
from employee.permission import UserPermission



class EmployeeListCreateAPIView(ListCreateAPIView):
    serializer_class = EmployeeSerializer
    queryset = Employee.objects.filter()

    def get_permissions(self):
        if self.request.method == 'POST':
            return (UserPermission('can_get_users'),)

        elif self.request.method == 'GET':
            return (permissions.AllowAny(),)
        raise MethodNotAllowed(method=self.request.method)
    
    # def get_permissions(self):
    #     if self.request.method == 'POST':
    #         return (permissions.AllowAny(),)
    #     elif self.request.method == 'GET':
    #         return (UserPermission('can_get_users'),)
    #     raise MethodNotAllowed(method=self.request.method)
