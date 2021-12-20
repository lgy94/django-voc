from django.db import models

# Create your models here.


class Categorylist(models.Model):
    id = models.AutoField(primary_key=True,null=False)
    service_name = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now=True)
