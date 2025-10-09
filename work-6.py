def obtener_distribucion_combustible(num_etapas):
    distribuciones = {
        1: [100],
        2: [85, 15],
        3: [80, 15, 5],
        4: [78, 12, 7, 3],
        5: [75, 12, 7, 4, 2]
    }
    return distribuciones.get(num_etapas)

def calcular_eficiencia(num_etapa, total_etapas):
    eficiencia_base = 0.5
    return eficiencia_base + (num_etapa/total_etapas * 2)

def calcular_tiempo_etapa(num_etapa):
    return 180 - (num_etapa - 1) * 30

def simular_etapa(etapa_actual, cant_comb, comb_restante, porcentaje, total_etapas):
    comb_cons = int((porcentaje/100) * cant_comb)
    
    if comb_cons > comb_restante:
        return {
            "error": True,
            "mensaje": f"Combustible insuficiente. Se necesitan {comb_cons} toneladas pero solo quedan {comb_restante} toneladas"
        }
    
    eficiencia = calcular_eficiencia(etapa_actual, total_etapas)
    tiempo_etapa = calcular_tiempo_etapa(etapa_actual)
    
    factor_conversion = 0.05 
    factor_gravedad = 0.7    
    factor_altura = 1 + (etapa_actual/total_etapas * 0.5)  
    
    distancia_etapa = (comb_cons * factor_conversion * eficiencia * factor_altura) * factor_gravedad
    velocidad_etapa = distancia_etapa / tiempo_etapa if tiempo_etapa > 0 else 0
    comb_restante -= comb_cons

    return {
        "error": False,
        "combustible_consumido": comb_cons,
        "porcentaje": porcentaje,
        "eficiencia": eficiencia,
        "tiempo": tiempo_etapa,
        "distancia": distancia_etapa,
        "velocidad": velocidad_etapa,
        "combustible_restante": comb_restante
    }

def mostrar_datos_etapa(num_etapa, datos):
    print(f"\nEtapa {num_etapa}:")
    print(f"  Porcentaje de combustible: {datos['porcentaje']}%")
    print(f"  Combustible consumido: {datos['combustible_consumido']} toneladas")
    print(f"  Combustible restante: {datos['combustible_restante']} toneladas")
    print(f"  Distancia recorrida: {datos['distancia']:.2f} km")
    print(f"  Velocidad: {datos['velocidad']:.2f} km/s")

def determinar_orbita(distancia):
    if distancia < 100:
        return "No alcanzó el espacio (< 100 km)"
    elif distancia < 200:
        return "Línea de Kármán - Inicio del espacio (100-200 km)"
    elif distancia < 2000:
        return "Órbita terrestre baja - LEO (200-2,000 km)"
    elif distancia < 35786:
        return "Órbita terrestre media - MEO (2,000-35,786 km)"
    elif distancia < 35786 * 2:
        return "Órbita geosincrónica - GEO (~35,786 km)"
    elif distancia < 384400:  
        return "Camino a la Luna (35,786 - 384,400 km)"
    elif distancia < 384400 + 10000:  
        return "¡Órbita lunar alcanzada! (~ 384,400 km)"
    else:
        return "Espacio profundo (> 384,400 km)"

def simular_cohete():
    while True:
        cant_etapas = int(input("Ingrese el número de etapas del cohete (1-5): "))
        if 1 <= cant_etapas <= 5:
            break
        print("Error: El número de etapas debe estar entre 1 y 5")

    while True:
        cant_comb = int(input("Ingrese la cantidad inicial de combustible (toneladas): "))
        if cant_comb < 1000:
            print("\nAdvertencia: Con menos de 1,000 toneladas de combustible, ")
            print("el cohete podría no alcanzar el espacio (100 km de altura)")
            confirmar = input("¿Desea continuar anyway? (s/n): ")
            if confirmar.lower() != 's':
                continue
        break
    
    print("\nValores recomendados de referencia:")
    print("- Cohete pequeño (órbita baja): 1,000-2,000 toneladas")
    print("- Cohete mediano (órbita media): 2,000-5,000 toneladas")
    print("- Cohete grande (órbita geoestacionaria): 5,000-10,000 toneladas")
    
    comb_restante = cant_comb
    distancia_total = 0
    velocidad_total = 0
    etapas_data = {}
    
    porcentajes = obtener_distribucion_combustible(cant_etapas)
    
    for etapa_actual in range(1, cant_etapas + 1):
        datos_etapa = simular_etapa(
            etapa_actual,
            cant_comb,
            comb_restante,
            porcentajes[etapa_actual - 1],
            cant_etapas
        )
        
        if datos_etapa.get("error"):
            print(f"\nAdvertencia: {datos_etapa['mensaje']}")
            break
            
        comb_restante = datos_etapa['combustible_restante']
        distancia_total += datos_etapa['distancia']
        velocidad_total += datos_etapa['velocidad']
        
        etapas_data[etapa_actual] = datos_etapa
        mostrar_datos_etapa(etapa_actual, datos_etapa)

    print(f"\nResumen del vuelo:")
    print(f"Distancia total recorrida: {distancia_total:.2f} km")
    print(f"Velocidad final: {velocidad_total:.2f} km/s")
    print(f"Órbita alcanzada: {determinar_orbita(distancia_total)}")
    
    if distancia_total >= 100:
        print("\n¡Éxito! El cohete ha alcanzado el espacio (>100 km)")
    else:
        print("\nEl cohete no alcanzó el espacio (<100 km)")

if __name__ == "__main__":
    simular_cohete()