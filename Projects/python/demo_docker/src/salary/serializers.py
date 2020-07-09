from rest_framework import serializers

from salary.models import Salary

class SalarySerializer(serializers.ModelSerializer):


		class Meta:
			model = Salary
			fields =  ['id','employee','house_rent','medical','transport','other','bonus','over_time','deduction', 'Salary_disburse', 'Salary_disburse_month']

