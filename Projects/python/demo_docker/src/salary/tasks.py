from typing import Dict
import time

from celery import shared_task
from salary.serializers import SalarySerializer
from salary.models import Salary


# @shared_task(name='create_project_detail')
# def create_project_detail(data: Dict) -> None:
#     time.sleep(3)
#     print('saved Project Detail task started!!')
#     serializer = ProjectDetailSerializer(data=data)
#     if serializer.is_valid(raise_exception=True):
#         serializer.save()
#     print('saved Project Detail task done!!')


@shared_task(name='get_total_salary')
def get_total_salary():
    time.sleep(3)
    print('saved salary task started!!')

    salaries                    = Salary.objects.all()
    for salary in salaries:
        salary.Salary_disburse  = salary.house_rent + salary.medical + salary.other + salary.house_rent + salary.bonus
        salary.save()
        serializer          = SalarySerializer(data=salary)
        if serializer.is_valid():
            serializer.save()
        
    print('saved Project Detail task done!!')    
