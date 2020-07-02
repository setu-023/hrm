from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, CreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView
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

    def list(self, request):
        queryset = self.get_queryset()
        serializer = EmployeeSerializer(queryset, many=True)
        return Response({ "response": status.HTTP_200_OK,"message":"showing data","data":serializer.data}) 
           

# class EmployeeRetrieveUpdateAPIView(RetrieveUpdateAPIView):
#     permission_classes = (permissions.AllowAny, )
#     serializer_class = EmployeeSerializer()
#     queryset = Employee.objects.filter()
#     lookup_field = 'id'

class EmployeeRetrieveUpdateAPIView(RetrieveUpdateDestroyAPIView):
    
    permission_classes = (permissions.AllowAny, )
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    lookup_field = 'id'



class EmployeeListAPIView(ListAPIView):
    
    serializer_class = EmployeeSerializer
    queryset = Employee.objects.filter()
    permission_classes = (permissions.AllowAny, )


    def list(self, request):
        user = Employee.objects.get( employee_id = request.user.id)
        serializer = EmployeeSerializer(user)
        return Response({ "response": status.HTTP_200_OK,"message":"showing data","data":serializer.data}) 
        
