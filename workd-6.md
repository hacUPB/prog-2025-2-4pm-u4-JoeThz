

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