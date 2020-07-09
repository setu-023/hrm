from rest_framework import serializers

from projec_detail.models import ProjectDetail

class ProjectDetailSerializer(serializers.ModelSerializer):
	
    class Meta:
        model   = ProjectDetail
        fields  = ['project','employee','dept_branch','role']
        
