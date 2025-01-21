from django.db import models

class Parcels(models.Model):
    doc_num = models.CharField(max_length=100)
    file_date = models.CharField(max_length=100)
    agmt_type = models.CharField(max_length=100)
    dv_url = models.CharField(max_length=100)
    classdesc = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    schooldesc = models.CharField(max_length=100)
    munidesc = models.CharField(max_length=100)
    pin = models.CharField(max_length=100)
    bk_vol_pg = models.CharField(max_length=100)
    usedesc = models.CharField(max_length=100)
    calcacreag = models.CharField(max_length=100)
    fairmarkettotal = models.CharField(max_length=100)
    filedate = models.CharField(max_length=100)

    # geomjson = models.TextField()

    # class Meta:
    #     # if managed = False then the model/table will not be added to the sqlite db 
    #     managed = False
    #     db_table = 'leasemap_parcels_wd'
    
    def __str__(self) -> str:
        return self.pin
    