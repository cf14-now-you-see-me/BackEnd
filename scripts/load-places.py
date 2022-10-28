from api.models import *
import csv

def run():
    Place.objects.all().delete()
    Amenity.objects.all().delete()
    with open("api/wisata.csv") as f:
        reader = csv.reader(f)
        next(reader)

        for row in reader:
            wisata = Place(
                name=row[1],
                google_id=row[2],
                location=row[3],
                ticket_price=row[4],
                description=row[5],
                long_description=row[6],
            )
            print(wisata)
            wisata.save()
    with open("api/amenity.csv") as f:
        reader = csv.reader(f)
        next(reader)

        for row in reader:
            if row[1] == 'Restoran':
                kind = 1
            else:
                kind = 0
            amenity = Amenity(
                name=row[0],
                kind=kind,
                info=row[5],
                near=Place.objects.filter(name=row[4]).first()
            )
            print(amenity)
            amenity.save()

run()