from django.db import models
from django.shortcuts import render, redirect

from base.models import BaseModel

class Activity(BaseModel):

    employee 	        = models.ForeignKey(to='employee.Employee', on_delete=models.CASECADE)
    attendance          = models.IntegerField()
    late_attendance     = models.IntegerField()
    assign_task         = models.ForeignKey(to='project.Project', on_delete=models.CASECADE)
    note                = models.CharField(max_length=255 )
    leave               = models.IntegerField()
    date                = models.DateTimeField(max_length=255 )


    def __str__(self):
        return self.name
