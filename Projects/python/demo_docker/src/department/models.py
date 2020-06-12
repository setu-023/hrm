from django.db import models

from base.models import BaseModel

class Department(BaseModel):

    name = models.CharField(max_length=255, )
    description = models.TextField(null=True)

 
    class Meta:
        db_table = 'departments'

    def __str__(self):
        return str(self.name)