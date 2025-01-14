# from db import postgreSQL, influxDB
# from ui import grafana

# #Levanto las bdd
# postgreSQL.run("psqlcivilizationsimulator")
# influxDB.run("influxcivilizationsimulator")

# #Agrego los Data Source
# postgrePayload = {
#     "name": "PostgreSQL-CivilizationSimulator",
#     "type": "postgres",
#     "url": "localhost:5432",
#     "access": "proxy",
#     "basicAuth": False,
#     "database": "psqlcivilizationsimulator",
#     "user": "emiliano",
#     "secureJsonData": {
#         "password": "Emiliano123"
#     },
#     "jsonData": {
#         "sslmode": "disable"  
#     }
# }
# #grafana.addDataSource(postgrePayload)

# influxPayload = {
#     "name": "InfluxDB-CivilizationSimulator",  # Nombre del DataSource
#     "type": "influxdb",  # Tipo de DataSource
#     "url": "http://localhost:8086",  # URL de InfluxDB
#     "access": "proxy",  # Método de acceso
#     "isDefault": True,  # Hacerlo DataSource por defecto
#     "jsonData": {
#         "httpMode": "GET",  # Modo de petición (GET o POST)
#         "timeInterval": "60s",  # Intervalo de tiempo por defecto
#         "organization": "Netlabs",  # Organización de InfluxDB
#         "bucket": "influxcivilizationsimulator",  # Bucket de InfluxDB
#         "language" :"flux"
#     },
#     "secureJsonData": {
#         "token": "QPHFtZ-X-ntdJNhqrf07T16cIOwtyIN0YRrb7diLW4VMK5uwScZd7offNrwpWeZznK-10WM1MXukFZmI6zZ4gw=="  # Token de autenticación de InfluxDB
#     }
# }
# grafana.addDataSource(influxPayload)