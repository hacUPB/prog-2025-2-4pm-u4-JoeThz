import random
# Crear una lista vacia.
lista = []

# Añadir un elemento a la lista.
lista.append(56)
print(lista)

# Añadir un elemento que ingrese el usuario a la lista.
numero = int(input("Ingrese un número: "))
lista.append(numero)
print (lista)

# Ingresar 10 números aleatorios a la lista.
for i in range(10):    
    aleat = random.randint(0,100)
    lista.append(aleat)
print(lista)

#