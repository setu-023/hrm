from django.db import models


class BaseModel(models.Model):

    #updated_by      = models.CharField(max_length=200)
    created_at      = models.DateTimeField(auto_now_add=True)
    updated_at      = models.DateTimeField(auto_now=True)
    status          = models.IntegerField(default = 1)
    
    class Meta:
        abstract = True