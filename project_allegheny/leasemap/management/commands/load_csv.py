import csv
from django.core.management.base import BaseCommand
from leasemap.models import Parcels

csv.field_size_limit(100000000)

class Command(BaseCommand):
    help = 'Loads data from a CSV file into the Person model'

    def handle(self, *args, **kwargs):
        # Path to the CSV file on your D: drive
        file_path = r'C:/projects/tmp_dbmigration/parcel_details_202501020016.csv'

        # Open the CSV file
        with open(file_path, mode='r') as file:
            csv_reader = csv.reader(file)
            # Skip the header if there is one
            next(csv_reader)

            # Loop through the CSV rows and add to the database
            for row in csv_reader:
                doc_num,file_date,agmt_type,dv_url,classdesc,company,schooldesc,munidesc,pin,bk_vol_pg,usedesc,calcacreag,fairmarkettotal = row
                # Create and save a Person object
                Parcels.objects.create(
                    doc_num=doc_num,
                    file_date=file_date,
                    agmt_type=agmt_type,
                    dv_url=dv_url,
                    classdesc=classdesc,
                    company=company,
                    schooldesc=schooldesc,
                    munidesc=munidesc,
                    pin=pin,
                    bk_vol_pg=bk_vol_pg,
                    usedesc=usedesc,
                    calcacreag=calcacreag,
                    fairmarkettotal=fairmarkettotal,
                )

        self.stdout.write(self.style.SUCCESS('Successfully loaded data from CSV'))
