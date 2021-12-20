from django.db import models

# Create your models here.
from categoryapp.models import Categorylist

class Voclist(models.Model):

    voc_no = models.AutoField(primary_key=True)
    voc_date = models.DateTimeField()
    voc_method = models.CharField(max_length=50)
    client_number = models.TextField()
    client_name = models.TextField()
    voc_number =  models.TextField()
    voc_title = models.TextField()
    voc_content = models.TextField()
    voc_comment = models.TextField()
    voc_manger = models.CharField(max_length=50)
    report = models.CharField(max_length=50)
    partner = models.CharField(max_length=50)
    category_num = models.ForeignKey(Categorylist, on_delete=models.CASCADE,null=True)

    def client_save(self):
        self.save()
