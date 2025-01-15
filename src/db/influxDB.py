from influxdb_client import InfluxDBClient
from influxdb_client.client.write_api import SYNCHRONOUS
import time

token = ""
org = "Netlabs"
url = "http://localhost:8086"
client = InfluxDBClient(url=url, token=token, org=org)
write_api = client.write_api(write_options=SYNCHRONOUS)
bucketName = "influxcivilizationsimulator"

def cargarDatos(point):
    write_api.write(bucket=bucketName, org=org,record=point)