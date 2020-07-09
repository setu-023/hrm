from typing import Dict
import time

from celery import shared_task
from projec_detail.serializers import ProjectDetailSerializer


@shared_task(name='test_celery')
def test_celery(data: Dict) -> None:
    time.sleep(5)
    print(data)


@shared_task(name='create_project_detail')
def create_project_detail(data: Dict) -> None:
    time.sleep(3)
    print('saved Project Detail task started!!')
    serializer = ProjectDetailSerializer(data=data)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
    print('saved Project Detail task done!!')