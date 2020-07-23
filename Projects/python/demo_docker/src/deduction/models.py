from django.db import models
from django.shortcuts import render, redirect

from base.models import BaseModel

class Deduction(BaseModel):

    employee 	             = models.ForeignKey(to='employee.Employee', on_delete = models.CASCADE)
    note                     = models.CharField(max_length=300)
    amount                   = models.IntegerField()


    def __str__(self):
        return self.name

    class Meta:
        db_table = 'deductions'
