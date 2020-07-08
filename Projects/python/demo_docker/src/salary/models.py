from django.db import models
from django.shortcuts import render, redirect

from base.models import BaseModel

class Salary(BaseModel):

    employee 	             = models.ForeignKey(to='employee.Employee', on_delete=models.CASCADE)
    house_rent               = models.IntegerField(default=0)
    medical                  = models.IntegerField(default=0)
    transport                = models.IntegerField(default=0)
    other                    = models.IntegerField(default=0)
    bonus                    = models.IntegerField(default=0)
    over_time                = models.IntegerField(default=0)
    deduction                = models.IntegerField(default=0)
    Salary_disburse          = models.IntegerField(default=0)
    Salary_disburse_month    = models.IntegerField()

    # def __str__(self):
    #     return self.employee.name
