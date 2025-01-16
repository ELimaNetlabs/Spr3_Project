from db import postgreSQL, influxDB
from influxdb_client import Point

def eventoGuerra(civ1, civ2, resultado):
    if resultado == 1: #Victoria
        postgreSQL.updateTableCivilization(civ1, 6, 2)  # Aumenta el ejército del ganador.
        postgreSQL.updateTableCivilization(civ2, 8, 1)  # Disminuye el ejército del perdedor.
        postgreSQL.updateTableCivilization(civ2, 10, 2000)  # Disminuye población del perdedor.
    elif resultado == 0: #Derrota
        postgreSQL.updateTableCivilization(civ2, 6, 2)  # Aumenta el ejército del ganador.
        postgreSQL.updateTableCivilization(civ1, 8, 1)  # Disminuye el ejército del perdedor.
        postgreSQL.updateTableCivilization(civ1, 10, 2000)  # Disminuye población del perdedor.
        influxDB.cargarDatos(Point("guerra").tag("civ1", civ1).tag("civ2", civ2).field("resultado", resultado))

def eventoAvanceTecnologico(civ, inteligencia_aumento, poder_monetario_aumento):
    postgreSQL.updateTableCivilization(civ, 5, inteligencia_aumento)  # Aumenta la inteligencia.
    postgreSQL.updateTableCivilization(civ, 4, poder_monetario_aumento)  # Incrementa el poder monetario.
    influxDB.cargarDatos(Point("avance_tecnologico").tag("civilizacion", civ).field("inteligencia", inteligencia_aumento).field("poder_monetario", poder_monetario_aumento))

def eventoDesastreNatural(civ, perdida_poblacion, perdida_recursos):
    postgreSQL.updateTableCivilization(civ, 10, perdida_poblacion)  # Reduce la población.
    influxDB.cargarDatos(Point("desastre_natural").tag("civilizacion", civ).field("poblacion_perdida", perdida_poblacion).field("recursos_perdidos", perdida_recursos))

def eventoCrecimientoPoblacional(civ, incremento_poblacion):
    postgreSQL.updateTableCivilization(civ, 7, incremento_poblacion)  # Incrementa la población.
    influxDB.cargarDatos(Point("crecimiento_poblacional").tag("civilizacion", civ).field("incremento_poblacion", incremento_poblacion))

def eventoComercio(civ1, civ2, cantidad_oro):
    postgreSQL.updateTableCivilization(civ1, 9, cantidad_oro)  # Reduce el oro de la civilización 1.
    postgreSQL.updateTableCivilization(civ2, 4, cantidad_oro)  # Aumenta el oro de la civilización 2.
    influxDB.cargarDatos(Point("comercio").tag("civ1", civ1).tag("civ2", civ2).field("cantidad_oro", cantidad_oro))

def eventoFormacionAlianza(civ1, civ2, nivel):
    postgreSQL.updateTableAliados(civ1, civ2, 3, nivel)  # Registra una nueva alianza.
    influxDB.cargarDatos(Point("alianza").tag("civ1", civ1).tag("civ2", civ2).field("nivel", nivel))