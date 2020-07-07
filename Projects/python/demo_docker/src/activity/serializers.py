from rest_framework import serializers

from activity.models import Activity

class BranchSerializer(serializers.ModelSerializer):
	
    class Meta:
        model = Activity
        fields = '__all__'
        
