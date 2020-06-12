from django.db import models

from base.models import BaseModel


class Branch(BaseModel):

    name        = models.CharField(max_length=255)
    description = models.TextField(null=True)
    address     = models.TextField(null=True)

 
    class Meta:
        db_table = 'branches'

    def __str__(self):
        return str(self.name)