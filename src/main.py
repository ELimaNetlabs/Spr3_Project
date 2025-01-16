import eventsManager as em
import os,time,random
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

    # Llamada aleatoria a eventos
    for turno in range(1, 11):  # 10 turnos de simulación
        print(f"\nTurno {turno}")
        
        evento_aleatorio = random.choice(['guerra', 'avance_tecnologico', 'desastre_natural', 'crecimiento_poblacional', 'comercio', 'formacion_alianza'])
        
        if evento_aleatorio == 'guerra':
            
            civ1 = random.randint(1,10)
            civ2 = random.randint(1,10)
            if civ1 == civ2:
                civ2 += 1
            resultado = random.randint(0,2)  # 0: Derrota, 1: Victoria
            print(f"Evento: Guerra entre {civ1} y {civ2}. Resultado: {'Victoria' if resultado == 1 else 'Derrota'}")
            em.eventoGuerra(civ1, civ2, resultado)
        
        elif evento_aleatorio == 'avance_tecnologico':
            # Se elige una civilización aleatoria y se le asignan incrementos aleatorios en tecnología
            civ = random.randint(1,10)
            inteligencia_aumento = random.randint(1, 5)
            poder_monetario_aumento = random.randint(100, 1000)
            print(f"Evento: Avance tecnológico en {civ}. Incrementos: Inteligencia +{inteligencia_aumento}, Poder Monetario +{poder_monetario_aumento}")
            em.eventoAvanceTecnologico(civ, inteligencia_aumento, poder_monetario_aumento)
        
        elif evento_aleatorio == 'desastre_natural':
            # Se elige una civilización aleatoria para el desastre natural
            civ = random.randint(1,10)
            perdida_poblacion = random.randint(1000, 10000)
            perdida_recursos = random.randint(500, 5000)
            print(f"Evento: Desastre natural en {civ}. Pérdida de población: {perdida_poblacion}, Pérdida de recursos: {perdida_recursos}")
            em.eventoDesastreNatural(civ, perdida_poblacion, perdida_recursos)
        
        elif evento_aleatorio == 'crecimiento_poblacional':
            # Se elige una civilización aleatoria para el crecimiento poblacional
            civ = random.randint(1,10)
            incremento_poblacion = random.randint(1000, 5000)
            print(f"Evento: Crecimiento poblacional en {civ}. Incremento: {incremento_poblacion}")
            em.eventoCrecimientoPoblacional(civ, incremento_poblacion)
        
        elif evento_aleatorio == 'comercio':
            # Se eligen dos civilizaciones aleatorias para un evento de comercio
            civ1 = random.randint(1,10)
            civ2 = random.randint(1,10)
            if civ1 == civ2:
                civ2 += 1
            cantidad_oro = random.randint(100, 1000)
            print(f"Evento: Comercio entre {civ1} y {civ2}. Cantidad de oro intercambiado: {cantidad_oro}")
            em.eventoComercio(civ1, civ2, cantidad_oro)
        
        elif evento_aleatorio == 'formacion_alianza':
            # Se eligen dos civilizaciones aleatorias para formar una alianza
            civ1 = random.randint(1,10)
            civ2 = random.randint(1,10)
            if civ1 == civ2:
                civ2 += 1
            nivel = random.randint(1, 5)  # El nivel de la alianza puede ser aleatorio
            print(f"Evento: Formación de alianza entre {civ1} y {civ2}. Nivel de la alianza: {nivel}")
            em.eventoFormacionAlianza(civ1, civ2, nivel)
        
        # Introducimos un retraso para que los eventos se vean con tiempo
        tiempo_espera = random.uniform(1, 3)  # Espera aleatoria entre 1 y 3 segundos
        time.sleep(tiempo_espera)




if __name__ == "__main__":
    menu_principal()