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
            return (UserPermission('can_create_emplooye'),)

        elif self.request.method == 'GET':
            return (permissions.AllowAny(),)
        raise MethodNotAllowed(method=self.request.method)

    def create(self, request, *args, **kwargs):

        serializer                   = EmployeeSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status':'201', 'msg': 'created successfully', 'data':serializer.data, }, status.HTTP_201_CREATED,)
        return Response({'status':'400', 'msg': 'Please Insert Correct value', 'data':serializer.errors, }, status.HTTP_400_BAD_REQUEST,)  
       
    def list(self, request):

        queryset = self.get_queryset()
        serializer = EmployeeSerializer(queryset, many=True)
        return Response({ "response": status.HTTP_200_OK,"message":"showing data","data":serializer.data}) 

class EmployeeRetrieveUpdateAPIView(RetrieveUpdateDestroyAPIView):
    
    permission_classes = (permissions.AllowAny, )
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    lookup_field = 'pk'

    def get_permissions(self):
        if self.request.method   == 'PUT' or self.request.method == 'PATCH':
            return (UserPermission('can_create_emplooye'),)

        elif self.request.method == 'GET':
            return (permissions.AllowAny(),)
        raise MethodNotAllowed(method=self.request.method)

    def get(self, request, pk, *args, **kwargs):

        employee        = Employee.objects.get(id=pk)
        serializer      = EmployeeSerializer(employee)

        return Response({'status':'200', 'msg': 'showing data', 'data':serializer.data, }, status.HTTP_200_OK,)
   
    def put(self,request,pk,format=None):
        employee        = Employee.objects.get(id=pk)
        serializer      = EmployeeSerializer(employee, data=request.data , partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response({'status':'200', 'msg': 'data updated', 'data':serializer.data, }, status.HTTP_200_OK,)

        return Response({'status':'400', 'msg': 'Please Insert Correct value', 'data':serializer.errors, }, status.HTTP_400_BAD_REQUEST,)  

class EmployeeListAPIView(ListAPIView):
    
    serializer_class = EmployeeSerializer
    queryset = Employee.objects.filter()
    permission_classes = (permissions.AllowAny, )


    def list(self, request):
        user = Employee.objects.get( employee_id = request.user.id)
        serializer = EmployeeSerializer(user)
        return Response({ "response": status.HTTP_200_OK,"message":"showing data","data":serializer.data}) 
        
