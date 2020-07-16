from django.shortcuts import render

from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from rest_framework import permissions, status
from rest_framework.response import Response

from department.models import Department
from department.serializers import DepartmentSerializer
from department.permission import UserPermission



class DepartmentListCreateAPIView(ListCreateAPIView):
    serializer_class = DepartmentSerializer
    queryset = Department.objects.filter()

    def get_permissions(self):
        if self.request.method   == 'POST':
            return (UserPermission('can_create_dept'),)

        elif self.request.method == 'GET':
            return (permissions.AllowAny(),)
        raise MethodNotAllowed(method=self.request.method)

    def create(self, request, *args, **kwargs):

        serializer                   = DepartmentSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status':'201', 'msg': 'created successfully', 'data':serializer.data, }, status.HTTP_201_CREATED,)
        return Response({'status':'400', 'msg': 'Please Insert Correct value', 'data':serializer.errors, }, status.HTTP_400_BAD_REQUEST,)  
        
    def list(self, request, format=None):

        dept                    = Department.objects.all()
        serializer              = DepartmentSerializer(dept, many=True)

        return Response({'status':'200', 'msg': 'showing departments', 'data':serializer.data, }, status.HTTP_200_OK,)


class DepartmentRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = DepartmentSerializer
    queryset = Department.objects.all()
    lookup_field = 'pk'

    def get_permissions(self):
        if self.request.method   == 'PUT' or self.request.method == 'PATCH':
            return (UserPermission('can_create_dept'),)
        elif self.request.method == 'GET':
            return (permissions.AllowAny(),)
        raise MethodNotAllowed(method=self.request.method)

    def get(self, request, pk, *args, **kwargs):

        dept        = Department.objects.get(id=pk)
        serializer  = DepartmentSerializer(dept)

        return Response({'status':'200', 'msg': 'showing data', 'data':serializer.data, }, status.HTTP_200_OK,)
   
    def put(self,request,pk,format=None):
        dept        = Department.objects.get(id=pk)
        serializer  = DepartmentSerializer(dept, data=request.data , partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response({'status':'200', 'msg': 'showing data', 'data':serializer.data, }, status.HTTP_200_OK,)
