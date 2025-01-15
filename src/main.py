from db import postgreSQL, influxDB
from influxdb_client import Point
import os,time
def menu_principal():
    os.system('clear')
    print("Bienvenido...")
    print("Iniciar simulacion?")

    opcion = input("(S|N): ").strip().lower()

    if opcion == 's':
        iniciar_simulacion()
    elif opcion == 'n':
        os.system('clear')
        print("Que la Fuerza te acompañe...")
        return
    else:
        os.system('clear')
        print("Intenta de nuevo.")
        time.sleep(1)
        
        menu_principal()

def iniciar_simulacion():
    os.system('clear')
    print("*** Simulación iniciada ***")

def eventoGuerra(civ1, civ2, resultado):
    if resultado == "victoria":
        postgreSQL.updateTableCivilization(civ1, 6, 2)  # Aumenta el ejército del ganador.
        postgreSQL.updateTableCivilization(civ2, 6, -2)  # Disminuye el ejército del perdedor.
        postgreSQL.updateTableCivilization(civ2, 7, -20000)  # Disminuye población del perdedor.
    elif resultado == "derrota":
        postgreSQL.updateTableCivilization(civ2, 6, 2)  # Aumenta el ejército del ganador.
        postgreSQL.updateTableCivilization(civ1, 6, -2)  # Disminuye el ejército del perdedor.
        postgreSQL.updateTableCivilization(civ1, 7, -20000)  # Disminuye población del perdedor.
        influxDB.cargarDatos(Point("guerra").tag("civ1", civ1).tag("civ2", civ2).field("resultado", resultado))

def eventoAvanceTecnologico(civ, inteligencia_aumento, poder_monetario_aumento):
    postgreSQL.updateTableCivilization(civ, 5, inteligencia_aumento)  # Aumenta la inteligencia.
    postgreSQL.updateTableCivilization(civ, 4, poder_monetario_aumento)  # Incrementa el poder monetario.
    influxDB.cargarDatos(Point("avance_tecnologico").tag("civilizacion", civ).field("inteligencia", inteligencia_aumento).field("poder_monetario", poder_monetario_aumento))

def eventoDesastreNatural(civ, perdida_poblacion, perdida_recursos):
    postgreSQL.updateTableCivilization(civ, 7, -perdida_poblacion)  # Reduce la población.
    influxDB.cargarDatos(Point("desastre_natural").tag("civilizacion", civ).field("poblacion_perdida", perdida_poblacion).field("recursos_perdidos", perdida_recursos))

def eventoCrecimientoPoblacional(civ, incremento_poblacion):
    postgreSQL.updateTableCivilization(civ, 7, incremento_poblacion)  # Incrementa la población.
    influxDB.cargarDatos(Point("crecimiento_poblacional").tag("civilizacion", civ).field("incremento_poblacion", incremento_poblacion))

def eventoComercio(civ1, civ2, cantidad_oro):
    postgreSQL.updateTableCivilization(civ1, 4, -cantidad_oro)  # Reduce el oro de la civilización 1.
    postgreSQL.updateTableCivilization(civ2, 4, cantidad_oro)  # Aumenta el oro de la civilización 2.
    influxDB.cargarDatos(Point("comercio").tag("civ1", civ1).tag("civ2", civ2).field("cantidad_oro", cantidad_oro))

def eventoFormacionAlianza(civ1, civ2, nivel):
    postgreSQL.updateTableAliados(civ1, civ2, nivel)  # Registra una nueva alianza.
    influxDB.cargarDatos(Point("alianza").tag("civ1", civ1).tag("civ2", civ2).field("nivel", nivel))

if __name__ == "__main__":
    menu_principal()