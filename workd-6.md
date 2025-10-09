

cant_etapas = int(input("Ingrese el número de etapas del cohete: "))
cant_comb = int(input("Ingrese la cantidad inicial de combustible (m³): "))
comb_restante = cant_comb
            
for etapa_actual in range(1, cant_etapas + 1):
    comb_cons = int(input(f"Ingrese combustible consumido en etapa {etapa_actual} (m³): "))
    comb_restante -= comb_cons
                
    mensaje_etapa = (f"Etapa {etapa_actual}: Combustible restante = {comb_restante} m³")
    print(mensaje_etapa)
                
    if comb_restante <= 0:
        print("Advertencia: El cohete se ha quedado sin combustible")
         break

# Le pedí ayuda a la IA con el analisis.

Analisis:
1. Almacenamiento de datos de las etapas:

Listas: Puedo usar una lista para almacenar la cantidad de combustible consumido en cada etapa.

Tuplas: Si la cantidad de etapas es fija y conocida, podría usar una tupla en lugar de una lista para almacenar el combustible consumido. Las tuplas son inmutables, lo que significa que no se pueden modificar después de su creación.

Diccionarios: Un diccionario sería útil para almacenar información más detallada sobre cada etapa, como el combustible consumido, la duración de la etapa, o cualquier otra métrica relevante. La clave del diccionario podría ser el número de etapa.

# Le pedí ayuda a la IA para entender como relacionar los datos y con las variables.

# Pseudocódigo mejorado con almacenamiento de datos en listas y diccionarios:

INICIO
    // Solicitar al usuario la cantidad de etapas del cohete
    LEER cant_etapas
    
    // Solicitar al usuario la cantidad inicial de combustible
    LEER cant_comb
    
    // Inicializar el combustible restante con la cantidad inicial
    comb_restante = cant_comb
    
    // Inicializar la distancia recorrida
    distancia_recorrida = 0
    
    // Inicializar la velocidad actual
    velocidad_actual = 0
    
    // Inicializar un diccionario para almacenar datos de cada etapa
    etapas_data = {}
    
    // Bucle para cada etapa del cohete
    PARA etapa_actual DESDE 1 HASTA cant_etapas HACER
        // Solicitar al usuario el combustible consumido en la etapa actual
        LEER comb_cons
        
        // Solicitar al usuario la eficiencia de la etapa actual
        LEER eficiencia_etapa
        
        // Solicitar al usuario el tiempo de la etapa actual
        LEER tiempo_etapa
        
        // Calcular la distancia recorrida en la etapa actual
        distancia_etapa = comb_cons * eficiencia_etapa
        
        // Acumular la distancia recorrida
        distancia_recorrida = distancia_recorrida + distancia_etapa
        
        // Calcular la velocidad en la etapa actual
        SI tiempo_etapa > 0 ENTONCES
            velocidad_etapa = distancia_etapa / tiempo_etapa
        SINO
            velocidad_etapa = 0
        FINSI
        
        // Acumular la velocidad
        velocidad_actual = velocidad_actual + velocidad_etapa
        
        // Restar el combustible consumido del combustible restante
        comb_restante = comb_restante - comb_cons
        
        // Crear un diccionario para la etapa actual
        etapa_data = {
            "combustible_consumido": comb_cons,
            "eficiencia": eficiencia_etapa,
            "tiempo": tiempo_etapa,
            "distancia": distancia_etapa,
            "velocidad": velocidad_etapa,
            "combustible_restante": comb_restante
        }
        
        // Almacenar el diccionario de la etapa en el diccionario de etapas
        etapas_data[etapa_actual] = etapa_data
        
        // Crear un mensaje para la etapa actual
        mensaje_etapa = "Etapa " + etapa_actual + ": Combustible restante = " + comb_restante + " m³, Distancia recorrida = " + distancia_etapa + " km, Velocidad = " + velocidad_actual + " km/s"
        
        // Imprimir el mensaje de la etapa
        IMPRIMIR mensaje_etapa
        
        // Comprobar si el cohete se ha quedado sin combustible
        SI comb_restante <= 0 ENTONCES
            // Imprimir una advertencia
            IMPRIMIR "Advertencia: El cohete se ha quedado sin combustible"
            
            // Salir del bucle
            BREAK
        FINSI
    FINPARA
    
    // Imprimir la distancia total recorrida
    IMPRIMIR "El cohete ha recorrido una distancia total de " + distancia_recorrida + " km"
    
    // Imprimir la velocidad final del cohete
    IMPRIMIR "La velocidad final del cohete es de " + velocidad_actual + " km/s"
    
    // Imprimir la información de cada etapa usando el diccionario
    PARA etapa, data EN etapas_data HACER
        IMPRIMIR "Etapa " + etapa + ":"
        IMPRIMIR "  Combustible consumido: " + data["combustible_consumido"] + " m³"
        IMPRIMIR "  Eficiencia: " + data["eficiencia"] + " km/m³"
        IMPRIMIR "  Tiempo: " + data["tiempo"] + " segundos"
        IMPRIMIR "  Distancia: " + data["distancia"] + " km"
        IMPRIMIR "  Velocidad: " + data["velocidad"] + " km/s"
        IMPRIMIR "  Combustible restante: " + data["combustible_restante"] + " m³"
    FINPARA
FIN

# Código mejorado con almacenamiento de datos en listas y diccionarios:

cant_etapas = int(input("Ingrese el número de etapas del cohete: "))

cant_comb = int(input("Ingrese la cantidad inicial de combustible (m³): "))

comb_restante = cant_comb

distancia_recorrida = 0

velocidad_actual = 0

etapas_data = {}  

combustible_restante_por_etapa = []

distancias_por_etapa = []

velocidades_por_etapa = []

for etapa_actual in range(1, cant_etapas + 1):
    comb_cons = int(input(f"Ingrese combustible consumido en etapa))