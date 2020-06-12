from django.db import models
from django.shortcuts import render, redirect

from base.models import BaseModel

class Employee(BaseModel):

    name 	            = models.CharField(max_length=255)
    description         = models.TextField()
    start_date          = models.DateTimeField(verbose_name='joining date')
    end_date            = models.DateTimeField(verbose_name='joining date')
    budget              = models.IntegerField()
    
    def __str__(self):
        return self.name
