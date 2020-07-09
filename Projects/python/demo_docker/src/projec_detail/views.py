from django.shortcuts import render

from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView
from rest_framework import permissions, status
from rest_framework.response import Response

from projec_detail.models import ProjectDetail
from projec_detail.serializers import ProjectDetailSerializer
from projec_detail.tasks import create_project_detail, test_celery


class ProjectDetailListCreateAPIView(ListCreateAPIView):
    permission_classes = (permissions.AllowAny, )
    serializer_class = ProjectDetailSerializer
    queryset = ProjectDetail.objects.all()

    def create(self, request, *args, **kwargs):
        create_project_detail.delay(request.data)
        return Response({'cede':'200', 'message': 'Request is processing'}, status=status.HTTP_200_OK)

    def list(self, request, *args, **kwargs):
        test_celery.delay(10)
        return Response({'cede':'200', 'message': 'Request is processing'}, status=status.HTTP_200_OK)
