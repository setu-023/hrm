from rest_framework import serializers

from project.models import Project
from projectDetail.serializers import ProjectDetailSerializer

class ProjectSerializer(serializers.ModelSerializer):
	
    class Meta:
        model  = Project
        fields = '__all__'
        
class ProjectDetailSerializer(serializers.ModelSerializer):
    
    projectDetail     = ProjectDetailSerializer(many=True)

    class Meta:
        model   = Project
        fields  = ['id','name', 'projectDetail']
 