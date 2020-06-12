from django.db import models
from django.shortcuts import render, redirect

from base.models import BaseModel

class Employee(BaseModel):

    name                = models.CharField(max_length=250, unique=True)
    email 	            = models.ForeignKey(to='account.Account', on_delete=models.CASCADE)
    possition           = models.CharField(max_length=250, )
    posting             = models.ForeignKey(to='dept_branch.DeptBranch', on_delete = models.CASCADE)
    phone               = models.CharField(max_length=25, unique=True )
    address             = models.TextField()
    dob                 = models.CharField(max_length=25, unique=True )
    joining_date        = models.DateTimeField(verbose_name='joining date')
    
    def __str__(self):
        return self.name
