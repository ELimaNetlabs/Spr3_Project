from db import postgreSQL, influxDB
from ui import grafana

#Levanto las bdd
postgreSQL.run("psqlcivilizationsimulator")
#influxDB.run("influxcivilizationsimulator")

#Agrego los Data Source
postgrePayload = {
    "name": "PostgreSQL-CivilizationSimulator",
    "type": "postgres",
    "url": "localhost:5432",
    "access": "proxy",
    "basicAuth": False,
    "database": "psqlcivilizationsimulator",
    "user": "emiliano",
    "secureJsonData": {
        "password": "Emiliano123"
    },
    "jsonData": {
        "sslmode": "disable"  
    }
}
grafana.addDataSource(postgrePayload)
#grafana.editDashboard("fe9swpytiydq8c")
