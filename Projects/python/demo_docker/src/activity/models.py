from django.db import models
from django.shortcuts import render, redirect

from base.models import BaseModel

class Activity(BaseModel):

    employee 	        = models.ForeignKey(to='employee.Employee', on_delete=models.CASCADE)
    attendance          = models.IntegerField()
    late_attendance     = models.IntegerField()
    note                = models.CharField(max_length=255 )
    leave               = models.IntegerField()
    month               = models.DateTimeField()


