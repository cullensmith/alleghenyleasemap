import csv
from django.core.management.base import BaseCommand
from leasemap.models import PolygonShort

class Command(BaseCommand):
    help = 'Loads data from a CSV file into the Person model'

    def handle(self, *args, **kwargs):
        # Path to the CSV file on your D: drive
        file_path = r'C:/projects/allegheny_leasemap/csvs/short_geojson.csv'

        # Open the CSV file
        with open(file_path, mode='r') as file:
            csv_reader = csv.reader(file)
            # Skip the header if there is one
            next(csv_reader)

            # Loop through the CSV rows and add to the database
            for row in csv_reader:
                pin, geomjson, id = row
                # Create and save a Person object
                PolygonShort.objects.create(
                    pin=pin,
                    geomjson=geomjson,
                    id=id
                )

        self.stdout.write(self.style.SUCCESS('Successfully loaded data from CSV'))
