from django.shortcuts import render

from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from rest_framework import permissions, status
from rest_framework.response import Response

from dept_branch.models import DeptBranch
from dept_branch.serializers import DeptBranchSerializer
from dept_branch.permission import UserPermission

class DeptBranchListCreateAPIView(ListCreateAPIView):
    queryset = DeptBranch.objects.all()
    serializer_class = DeptBranchSerializer(queryset, many = True)


    def get_permissions(self):
        if self.request.method == 'POST':
            return (UserPermission('can_create_dept'),)

        elif self.request.method == 'GET':
            return (permissions.AllowAny(),)
        raise MethodNotAllowed(method=self.request.method)

    def create(self, request, *args, **kwargs):


        dept_branch = DeptBranch.objects.filter( dept = self.request.data['dept'], branch = self.request.data['branch']) 
        if dept_branch:
            return Response({'status':'405', 'msg': 'already assigned',}, status.HTTP_405_METHOD_NOT_ALLOWED,)

        serializer = DeptBranchSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status':'201', 'msg': 'department and branch assigned successfully', 'data': serializer.data },status=status.HTTP_201_CREATED)

        return Response({'status':'400', 'message': 'something went wrong', 'data' : serializer.errors}, status.HTTP_400_BAD_REQUEST,)

    
    def list(self, request, format=None):

        dept        = DeptBranch.objects.all()
        serializer  = DeptBranchSerializer(dept, many=True)

        return Response({'status':'200', 'msg': 'showing data', 'data':serializer.data, }, status.HTTP_200_OK,)


class DeptBranchRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = DeptBranchSerializer
    queryset = DeptBranch.objects.all()
    lookup_field = 'pk'

    def get_permissions(self):
        if self.request.method == 'PUT' or self.request.method == 'PATCH':
            return (UserPermission('can_create_dept'),)
        elif self.request.method == 'GET':
            return (permissions.AllowAny(),)
        raise MethodNotAllowed(method=self.request.method)

    def get(self, request, pk, *args, **kwargs):

        dept        = DeptBranch.objects.get(id=pk)
        serializer  = DeptBranchSerializer(dept)

        return Response({'status':'200', 'msg': 'showing data', 'data':serializer.data, }, status.HTTP_200_OK,)
   
    def put(self,request,pk,format=None):
        dept        = DeptBranch.objects.get(id=pk)
        serializer  = DeptBranchSerializer(dept, data=request.data , partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response({'status':'200', 'msg': 'showing data', 'data':serializer.data, }, status.HTTP_200_OK,)
