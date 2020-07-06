from django.shortcuts import render
from django.core.paginator import Paginator
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView, ListAPIView
from rest_framework import permissions, status
from rest_framework.response import Response

from rest_framework.pagination import PageNumberPagination

from branch.models import Branch
from branch.serializers import BranchSerializer
from branch.permission import UserPermission
from base.pagination import CustomPagination

class BranchListCreateAPIView(ListCreateAPIView):

    queryset = Branch.objects.all()
    serializer_class = BranchSerializer(queryset, many=True)


    def get_permissions(self):
        if self.request.method == 'POST':
            return (UserPermission('can_create_dept'),)

        elif self.request.method == 'GET':
            return (permissions.AllowAny(),)
        raise MethodNotAllowed(method=self.request.method)
   
   
    def create(self, request, *args, **kwargs):

        serializer    = BranchSerializer(request.data)
        #return Response({'message': 'Request is processing'}, status=status.HTTP_200_OK)
        return Response({'status':'201', 'msg': 'created successfully', 'data':serializer.data, }, status.HTTP_201_CREATED,)

    def list(self, request, format=None):

        queryset = Branch.objects.all()
        serializer    = BranchSerializer(queryset, many = True)

        return Response({'status':'200', 'msg': 'showing data', 'data':serializer.data, }, status.HTTP_200_OK,)


class BranchRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = BranchSerializer
    queryset = Branch.objects.all()
    lookup_field = 'pk'

    def get_permissions(self):
        if self.request.method == 'PUT' or self.request.method == 'PATCH':
            return (UserPermission('can_create_dept'),)
        elif self.request.method == 'GET':
            return (permissions.AllowAny(),)
        raise MethodNotAllowed(method=self.request.method)

    def get(self, request, pk, *args, **kwargs):

        branch              = Branch.objects.get(id=pk)
        serializer          = BranchSerializer(branch)

        return Response({'status':'200', 'msg': 'showing data', 'data':serializer.data, }, status.HTTP_200_OK,)
   
    def put(self,request,pk,format=None):
        branch        = Branch.objects.get(id=pk)
        serializer  = BranchSerializer(branch, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status':'200', 'msg': 'showing data', 'data':serializer.data, }, status.HTTP_200_OK,)


class BranchListAPIView(ListAPIView):

    queryset = Branch.objects.all()
    serializer_class = BranchSerializer
    permission_classes = (permissions.AllowAny, )

    pagination_class = PageNumberPagination  
