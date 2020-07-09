from django.shortcuts import render
from django.core.paginator import Paginator
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView, CreateAPIView
from rest_framework import permissions, status
from rest_framework.response import Response

from rest_framework.pagination import PageNumberPagination

from project.models import Project
from project.serializers import ProjectSerializer, ProjectWithDetailSerializer
from base.permission import UserPermission
from base.pagination import CustomPagination


class ProjectListCreateAPIView(ListCreateAPIView):

    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

    def get_permissions(self):
        if self.request.method == 'POST':
            return (UserPermission('can_create_dept'),)

        elif self.request.method == 'GET':
            return (permissions.AllowAny(),)
        raise MethodNotAllowed(method=self.request.method)
   
   
    # def create(self, request, *args, **kwargs):

    #     serializer    = ProjectSerializer(data=request.data)
    #     if serializer.is_valid():
    #         return Response({'status':'201', 'msg': 'created successfully', 'data':serializer.data, }, status.HTTP_201_CREATED,)
    #     else:
    #         return Response({'status':'500', 'msg': 'error',})

    def list(self, request, format=None):

        queryset      = Project.objects.all()
        serializer    = ProjectSerializer(queryset, many = True)

        return Response({'status':'200', 'msg': 'showing data', 'data':serializer.data, }, status.HTTP_200_OK,)

class ProjectRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = ProjectSerializer
    queryset = Project.objects.all()
    lookup_field = 'pk'

    def get_permissions(self):
        if self.request.method == 'PUT' or self.request.method == 'PATCH':
            return (UserPermission('can_create_dept'),)
        elif self.request.method == 'GET':
            return (permissions.AllowAny(),)
        raise MethodNotAllowed(method=self.request.method)

    def get(self, request, pk, *args, **kwargs):

        project              = Project.objects.get(id=pk)
        serializer           = ProjectSerializer(project)

        return Response({'status':'200', 'msg': 'showing data', 'data':serializer.data, }, status.HTTP_200_OK,)
   
    def put(self,request,pk,format=None):
        project        = project.objects.get(id=pk)
        serializer  = ProjectSerializer(project, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status':'200', 'msg': 'showing data', 'data':serializer.data, }, status.HTTP_200_OK,)

class ProjectCreateAPIView(ListCreateAPIView):

    queryset = Project.objects.all()
    serializer_class = ProjectWithDetailSerializer

    def get_permissions(self):
        if self.request.method == 'POST':
            return (UserPermission('can_create_dept'),)

        elif self.request.method == 'GET':
            return (permissions.AllowAny(),)
            
        raise MethodNotAllowed(method=self.request.method)
   
   
   
    def create(self, request, *args, **kwargs):

        serializer = ProjectWithDetailSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response({'status':'201', 'msg': 'created successfully', 'data':serializer.data, }, status.HTTP_201_CREATED,)
        return Response({'status':'500', 'msg': ' not okay', 'error':serializer.error},status.HTTP_201_CREATED)
    
    def list(self, request, format=None):

        queryset      = Project.objects.all()
        serializer    = ProjectWithDetailSerializer(queryset, many = True)

        return Response({'status':'200', 'msg': 'showing data', 'data':serializer.data, }, status.HTTP_200_OK,)
