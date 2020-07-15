from django.shortcuts import render
from django.core.paginator import Paginator

from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView, ListAPIView
from rest_framework import permissions, status
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination

from activity.models import Activity
from activity.serializers import ActivitySerializer
from base.permission import UserPermission

class ActivityListCreateAPIView(ListCreateAPIView):

    queryset = Activity.objects.filter()
    serializer_class = ActivitySerializer
    

    def get_permissions(self):
        if self.request.method == 'POST' :
            return (UserPermission('can_create_dept'),)

        elif self.request.method == 'GET':
            return (UserPermission('can_create_dept'),)
        raise MethodNotAllowed(method=self.request.method)
   
   
    def create(self, request, *args, **kwargs):

        serializer = ActivitySerializer(data=request.data)

        #ifserializer.is_valid(raise_exception=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'status':'201', 'msg': 'created successfully', 'data':serializer.data, }, status.HTTP_201_CREATED,)
        return Response({'code':'400', 'msg': serializer.errors }, status=status.HTTP_400_BAD_REQUEST)
    
    def list(self, request, format=None):

        queryset      = Activity.objects.all()
        serializer    = ActivitySerializer(queryset, many = True)

        return Response({'status':'200', 'msg': 'showing data', 'data':serializer.data, }, status.HTTP_200_OK,)


class ActivityRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = ActivitySerializer
    queryset =  Activity.objects.all()
    lookup_field = 'pk'

    def get_permissions(self):
        if self.request.method == 'PUT' or self.request.method == 'PATCH' :
            return (UserPermission('can_create_dept'),)
        elif self.request.method == 'GET':
            return (UserPermission('can_create_dept'),)
        raise MethodNotAllowed(method=self.request.method)

    def get(self, request, pk , format=None):

        activity              = Activity.objects.get(id=pk)
        serializer            = ActivitySerializer(activity)

        return Response({'status':'200', 'msg': 'showing data', 'data':serializer.data, }, status.HTTP_200_OK,)
   
    def put(self,request,pk,format=None):

        activity              = Activity.objects.get(id=pk)
        serializer            = ActivitySerializer(activity, data = request.data, partial = True)
        # return Response({'status':'200', 'msg': 'showing data', 'data':serializer.data, }, status.HTTP_200_OK,)
        if serializer.is_valid():
            serializer.save()
            return Response({'status':'200', 'msg': 'showing data', 'data':serializer.data, }, status.HTTP_200_OK,)
        else :
            return Response ({'data':pk})

class ActivityListAPIView(ListAPIView):
    
    serializer_class = ActivitySerializer
    queryset = Activity.objects.filter()
    permission_classes = (permissions.AllowAny, )


    def list(self, request):
        user = Activity.objects.get( employee = request.user.id)
        serializer = ActivitySerializer(user)
        return Response({ "response": status.HTTP_200_OK,"message":"showing data","data":serializer.data}) 
        
