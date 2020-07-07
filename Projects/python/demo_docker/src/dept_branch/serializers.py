from rest_framework import serializers

from dept_branch.models import DeptBranch

class DeptBranchSerializer(serializers.ModelSerializer):


		class Meta:
			model = DeptBranch
			fields =['id', 'dept', 'branch', 'total_emplooye', 'status']

   