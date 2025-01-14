from influxdb_client import InfluxDBClient, Point, WritePrecision
from influxdb_client.client.write_api import SYNCHRONOUS
import time

token = ""
org = "Netlabs"
url = "http://localhost:8086"
client = InfluxDBClient(url=url, token=token, org=org)
bucketName = ""

def run(bName):
    bucketName = bName
    buckets_api = client.buckets_api()

    bucket = buckets_api.create_bucket(
        bucket_name=bucketName,
        org=org,
        retention_rules=[{
            "type": "expire",
            "every_seconds": 0
        }]
    )
    print(f"Bucket '{bucket.name}' creado con éxito.")

def cargarDatos(point):
    write_api = client.write_api(write_options=SYNCHRONOUS)

    #Esto llega por parametro
    point = Point("temperatura") \
    .tag("ubicacion", "cuarto") \
    .field("valor", 27.3) 

    write_api.write(bucket=bucketName, org="Netlabs",record=point)