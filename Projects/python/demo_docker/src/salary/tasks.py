from typing import Dict
import time

from celery import shared_task
from salary.serializers import SalarySerializer
from salary.models import Salary


@shared_task
def get_total_salary():
    
    print('saved salary task started!!')

    salaries                    = Salary.objects.all()
    for salary in salaries:
        salary.Salary_disburse  = salary.house_rent + salary.medical + salary.other + salary.house_rent + salary.bonus
        salary.save()
        serializer          = SalarySerializer(data=salary)
        if serializer.is_valid():
            serializer.save()
        
    print('task done!!')    
