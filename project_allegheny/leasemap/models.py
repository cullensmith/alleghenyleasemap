from django.db import models

class PolygonModel(models.Model):
    # Define fields according to your database schema
    pin = models.CharField()
    geomjson = models.CharField()
    # field_2 = models.CharField(max_length=100)
    # field_5 = models.CharField(max_length=100)
    # propertycity = models.CharField(max_length=100)

    class Meta:
        managed = False  # This model does not have a database table as it's a view
        db_table = 'allegheny_polygons'  # Replace 'your_polygon_table' with your actual table name

class Parcels(models.Model):
    doc_num = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
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
    geomjson = models.CharField()

    class Meta:
        managed = False
        db_table = 'parcel_details'
    
    def __str__(self) -> str:
        return super().__str__()
    
class Wells_U(models.Model):
    permit_num = models.CharField(max_length=100)
    latitude = models.CharField(max_length=100)
    longitude = models.CharField(max_length=100)
    geomjson = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'wells_allegh_u'
    
    def __str__(self) -> str:
        return super().__str__()
    
class Wells_C(models.Model):
    permit_num = models.CharField(max_length=100)
    latitude = models.CharField(max_length=100)
    longitude = models.CharField(max_length=100)
    geomjson = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'wells_allegh_c'
    
    def __str__(self) -> str:
        return super().__str__()

# Create your models here.
class Wells15(models.Model):
    api_num = models.CharField(max_length=50, blank=True, null=True)
    other_id = models.CharField(max_length=50, blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    stusps = models.CharField(max_length=50, blank=True, null=True)
    county = models.CharField(max_length=50, blank=True, null=True)
    municipality = models.CharField(max_length=50, blank=True, null=True)
    well_name = models.CharField(max_length=50, blank=True, null=True)
    operator = models.CharField(max_length=50, blank=True, null=True)
    spud_date = models.CharField(max_length=50, blank=True, null=True)
    plug_date = models.CharField(max_length=50, blank=True, null=True)
    well_type = models.CharField(max_length=50, blank=True, null=True)
    well_status = models.CharField(max_length=50, blank=True, null=True)
    well_configuration = models.CharField(max_length=50, blank=True, null=True)
    ft_category = models.CharField(max_length=50, blank=True, null=True)
    wellwiki = models.CharField(max_length=50, blank=True, null=True)
    src_url = models.CharField(max_length=50, blank=True, null=True)
    ft_uid = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'wellsdb'
    
    def __str__(self) -> str:
        return super().__str__()
    


# Create your models here.
class Points(models.Model):
    api_num = models.CharField(max_length=50, blank=True, null=True)
    other_id = models.CharField(max_length=50, blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    stusps = models.CharField(max_length=50, blank=True, null=True)
    county = models.CharField(max_length=50, blank=True, null=True)
    municipality = models.CharField(max_length=50, blank=True, null=True)
    well_name = models.CharField(max_length=50, blank=True, null=True)
    operator = models.CharField(max_length=50, blank=True, null=True)
    spud_date = models.CharField(max_length=50, blank=True, null=True)
    plug_date = models.CharField(max_length=50, blank=True, null=True)
    well_type = models.CharField(max_length=50, blank=True, null=True)
    well_status = models.CharField(max_length=50, blank=True, null=True)
    well_configuration = models.CharField(max_length=50, blank=True, null=True)
    ft_category = models.CharField(max_length=50, blank=True, null=True)
    wellwiki = models.CharField(max_length=50, blank=True, null=True)
    src_url = models.CharField(max_length=50, blank=True, null=True)
    ft_uid = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'wells15'
    
    def __str__(self) -> str:
        return super().__str__()
    