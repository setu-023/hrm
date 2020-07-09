from rest_framework import serializers

from project.models import Project
from projec_detail.serializers import ProjectDetailSerializer
from projec_detail.models import ProjectDetail
from rest_framework.response import Response


class ProjectSerializer(serializers.ModelSerializer):
	
    class Meta:
        model  = Project
        fields = '__all__'
        
class ProjectWithDetailSerializer(serializers.ModelSerializer):
    
    projectDetail     = ProjectDetailSerializer(many=True)

    class Meta:
        model   = Project
        fields  = ['id', 'name','description','budget', 'start_date','end_date' ,'projectDetail']

    def create(self, validated_data):
        
        projectDetail_data = validated_data.pop('projectDetail')
        project_data = Project.objects.create(**validated_data)

        for info in projectDetail_data:
           
            ProjectDetail.objects.create(**info , project = project_data)
        return project_data
