from django.db import models

from base.models import BaseModel


class DeptBranch(BaseModel):

    dept            = models.ForeignKey(to='department.Department', on_delete=models.PROTECT)
    branch          = models.ForeignKey(to='branch.Branch', on_delete=models.PROTECT)
    total_emplooye  = models.IntegerField(default=0)

 
    class Meta:
        db_table = 'DeptBranch'

    # def __str__(self):
    #     return str(self.sku)