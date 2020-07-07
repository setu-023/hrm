from rest_framework import serializers

from salary.models import Salary

class BranchSerializer(serializers.ModelSerializer):
	
    class Meta:
        model = Salary
        fields = '__all__'
        
