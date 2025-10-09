#1**Análisis de eficiencia de combustible**
#Desarrolle una función que calcule la eficiencia de combustible de una aeronave a lo largo de diferentes etapas de vuelo.
def analizar_eficiencia(distancias, combustible_consumido):
    """
    Calcula la eficiencia de combustible en km/L para cada tramo del vuelo
    y devuelve estadísticas relevantes.

    Args:
        distancias: Lista de distancias recorridas en km por tramo
        combustible_consumido: Lista de combustible consumido en L por tramo

    Returns:
        Las estadísticas de eficiencia
    """
    # Su código aquí
    # 1. Calcular la eficiencia para cada tramo (distancia/combustible)
    # 2. Determinar tramo más eficiente y menos eficiente
    # 3. Calcular eficiencia promedio
    pass

# Datos de prueba
tramos_distancia = [800, 1200, 1000, 750]  # km
tramos_combustible = [2400, 3000, 2800, 2000]  # L

# Probando la función
# resultado = analizar_eficiencia(tramos_distancia, tramos_combustible)
# print(resultado)


#### Ejercicio 2: Selección de cajas para carga en una aeronave

#En una operación de carga aérea, se tiene una lista de cajas, cada una con un peso diferente. 
#La aeronave tiene un límite máximo de peso que no debe ser superado por la suma de los pesos de las cajas seleccionadas. 
#Debes escribir una función que recorra la lista de pesos de las cajas, agregue cada caja mientras no se exceda el peso máximo permitido. 
#La función debe mostrar en pantalla los índices de las cajas seleccionadas y el peso total cargado.

#Completa el código a continuación utilizando únicamente listas y ciclos:

def cargar_cajas(pesos, peso_maximo):
    """
    Selecciona cajas para cargar en la aeronave sin exceder el peso máximo.

    Args:
        pesos: lista de pesos de las cajas (kg)
        peso_maximo: peso máximo permitido (kg)
    """
    # Tu código aquí

# Datos de prueba
pesos_cajas = [120, 400, 300, 180, 450, 200]
peso_max_avion = 1000

cargar_cajas(pesos_cajas, peso_max_avion)


#### **Ejercicio 3: Análisis de trayectoria**

#Desarrolle una función que analice una trayectoria de vuelo y detecte desviaciones significativas del rumbo planeado.

def analizar_trayectoria(rumbo_planeado, rumbo_real, umbral_desviacion=5):
    """
    Identifica puntos en la trayectoria donde el avión se desvió
    significativamente del rumbo planeado.

    Args:
        rumbo_planeado: Lista de ángulos planeados (grados)
        rumbo_real: Lista de ángulos reales seguidos (grados)
        umbral_desviacion: Desviación máxima permitida en grados

    Returns:
        Lista de índices donde la desviación superó el umbral
    """
    # Su código aquí
    pass

# Datos de prueba
planeado = [45, 45, 45, 90, 90, 90, 180, 180, 225, 225, 270]
real = [43, 47, 48, 86, 91, 95, 183, 176, 222, 230, 265]

# Probando la función
# desviaciones = analizar_trayectoria(planeado, real, 5)
# print(f"Se detectaron desviaciones significativas en los puntos: {desviaciones}")