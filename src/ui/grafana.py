import requests
import json

grafana_url = "http://localhost:3000"
dataSource_url = f"{grafana_url}/api/datasources"
dashboard_url = f"{grafana_url}/api/dashboards"
api_key = ""

headers = {
    "Authorization": f"Bearer {api_key}",
    "Content-Type": "application/json"
}


def listDB():
    response = requests.get(dataSource_url, headers=headers)

    if response.status_code == 200:
        print("Conexión exitosa. Fuentes de datos configuradas:")
        for ds in response.json():
            print(f"- {ds['name']} (ID: {ds['id']})")
    else:
        print(f"Error conectando a la API de Grafana: {response.json()}")


def addDataSource(payload):
    response = requests.post(dataSource_url, headers=headers, data=json.dumps(payload))

    if response.status_code == 200:
        print("Datasource creado exitosamente:")
        print(response.json())
    else:
        print(f"Error al crear el datasource: {response.status_code}")
        print(response.json())


def editDashboard(uid):
    response = requests.get(f"{dashboard_url}/uid/{uid}", headers=headers)

    if response.status_code == 200:
        dashboard_data = response.json()
        dashboard_json = dashboard_data['dashboard']
        print(dashboard_json)
    else:
        print(f"Error: {response.status_code} - {response.text}")
