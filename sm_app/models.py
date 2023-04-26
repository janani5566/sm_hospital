from django.db import models

# Create your models here.

class IPModel(models.Model):

    ipno = models.CharField(max_length=200,default='some_value')
    perid = models.CharField(max_length=200,default='some_value')
    admitdate = models.CharField(max_length=200,default='some_value')
    dischargedate = models.CharField(max_length=200,default='some_value')
    doctorname = models.CharField(max_length=200,default='some_value')
    name = models.CharField(max_length=200)
    age = models.CharField(max_length=200)
    gender = models.CharField(max_length=200)
    adres = models.CharField(max_length=200)
    mobile = models.CharField(max_length=200)
    advance = models.CharField(max_length=200)
    roomtype = models.CharField(max_length=200)
    roomno = models.CharField(max_length=200)
    status = models.CharField(max_length=200)

    class Meta:
        db_table = 'IPInfo_tbl'

    def __str__ (self):
       return self.name
