import pymysql
from django.core.management.base import BaseCommand, CommandError
from language.models import Language, Community

import os
import sys
import json


class Client:
    def update(self):
        db = pymysql.connect(
            os.environ["ARTSMAP_HOST"],
            os.environ["ARTSMAP_USER"],
            os.environ["ARTSMAP_PW"],
            os.environ["ARTSMAP_DB"],
        )

        # prepare a cursor object using cursor() method
        cursor = db.cursor()

        # Prepare SQL query to INSERT a record into the database.
        # sql = "SELECT * FROM node \
        #     WHERE type = 'art'"
        # sql = "show tables;"
        sql = """
        select distinct node.type, node.title, location.latitude, location.longitude, node.nid
        from node inner join location_instance on node.nid=location_instance.nid
            inner join location on location.lid=location_instance.lid
        where node.type = 'art' or node.type = 'event' or node.type = 'profile' or node.type = 'org';
        """
        # Execute the SQL command
        cursor.execute(sql)
        # Fetch all the rows in a list of lists.
        results = cursor.fetchall()

        geojson = {"type": "FeatureCollection", "features": []}

        for row in results:
            if float(row[2]) and float(row[3]):  # only want spatial data.
                name = row[1].strip()
                if float(row[3]) > -110:
                    print(row[3], "is outside the allowable area for this map, skip.")
                    # skip any features that are past Alberta,
                    # there seems to be junk in the arts db.
                    continue
                if (
                    name.lower().endswith("band")
                    or name.lower().endswith("nation")
                    or name.lower().endswith("council")
                    or name.lower().endswith("nations")
                ):
                    # bands are duplicated in other layers, skip them.
                    print(row[1], "is duplicated in another layer, skip.")
                    continue
                geojson["features"].append(
                    {
                        "type": "Feature",
                        "properties": {
                            "type": row[0],
                            "title": name,
                            "node_id": row[4],
                        },
                        "geometry": {
                            "type": "Point",
                            "coordinates": [float(row[3]), float(row[2])],
                        },
                    }
                )
        return geojson


class Command(BaseCommand):
    help = "Closes the specified poll for voting"

    def handle(self, *args, **options):

        open("web/static/web/arts1.json", "w").write(json.dumps(Client().update()))
