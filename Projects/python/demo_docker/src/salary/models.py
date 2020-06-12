from django.db import models
from django.shortcuts import render, redirect

from base.models import BaseModel

class Salary(BaseModel):

    employee 	             = models.ForeignKey(to='employee.Employee', on_delete=models.CASCADE)
    house_rent               = models.IntegerField()
    medical                  = models.IntegerField()
    transport                = models.IntegerField()
    other                    = models.IntegerField()
    bonus                    = models.IntegerField()
    over_time                = models.IntegerField()
    deduction                = models.IntegerField()
    Salary_disburse          = models.IntegerField()
    Salary_disburse_month    = models.IntegerField()

    def __str__(self):
        return self.name
