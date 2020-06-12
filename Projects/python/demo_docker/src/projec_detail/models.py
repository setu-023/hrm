from django.db import models
from django.shortcuts import render, redirect

from base.models import BaseModel

class ProjectDetail(BaseModel):

    project         = models.ForeignKey(to='project.Project', on_delete=models.CASECADE)
    employee        = models.ForeignKey(to='employee.employee', on_delete=models.CASECADE)
    dept_branch     = models.ForeignKey(to='dept_branch.DeptBranch', on_delete=models.CASECADE)
    role            = models.CharField(max_length=100)
  

    def __str__(self):
        return self.name
