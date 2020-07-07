from django.shortcuts import render
from django.core.paginator import Paginator
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView, ListAPIView
from rest_framework import permissions, status
from rest_framework.response import Response

from rest_framework.pagination import PageNumberPagination

from salary.models import Salary
from salary.serializers import SalarySerializer
from base.permission import UserPermission

class SalaryListCreateAPIView(ListCreateAPIView):

    queryset = Salary.objects.all()
    serializer_class = SalarySerializer(queryset, many=True)
    
    def get_queryset(self):
        return Mmodel.objects.all()

    def get_permissions(self):
        if self.request.method == 'POST' :
            return (UserPermission('can_create_dept'),)

        elif self.request.method == 'GET':
            return (UserPermission('can_create_dept'),)
        raise MethodNotAllowed(method=self.request.method)
   
   
    def create(self, request, *args, **kwargs):

        serializer    = SalarySerializer(request.data)
        return Response({'status':'201', 'msg': 'created successfully', 'data':serializer.data, }, status.HTTP_201_CREATED,)

    def list(self, request, format=None):

        queryset      = Salary.objects.all()
        serializer    = SalarySerializer(queryset, many = True)

        return Response({'status':'200', 'msg': 'showing data', 'data':serializer.data, }, status.HTTP_200_OK,)


class SalaryRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = SalarySerializer
    queryset =  Salary.objects.all()
    lookup_field = 'pk'

    def get_permissions(self):
        if self.request.method == 'PUT' or self.request.method == 'PATCH' :
            return (UserPermission('can_create_dept'),)
        elif self.request.method == 'GET':
            return (UserPermission('can_create_dept'),)
        raise MethodNotAllowed(method=self.request.method)

    def get(self, request, pk , format=None):

        salary              = Salary.objects.get(id=pk)
        serializer          = SalarySerializer(salary)

        return Response({'status':'200', 'msg': 'showing data', 'data':serializer.data, }, status.HTTP_200_OK,)
   
    def put(self,request,pk,format=None):

        salary              = Salary.objects.get(id=pk)
        serializer          = SalarySerializer(salary, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status':'200', 'msg': 'showing data', 'data':serializer.data, }, status.HTTP_200_OK,)
        else :
            return Response ({'data':pk})

class SalaryListAPIView(ListAPIView):
   
    serializer_class = SalarySerializer
    queryset = Salary.objects.filter()
    permission_classes = (permissions.AllowAny, )


    def list(self, request):
        salary = Salary.objects.get( employee = request.user.id)
        serializer = SalarySerializer(salary)
        return Response({ "response": status.HTTP_200_OK,"message":"showing data","data":serializer.data}) 
        
