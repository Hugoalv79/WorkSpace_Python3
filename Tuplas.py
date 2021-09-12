first_tuple = ("Naranja", "Platano", "Guayaba")

# Saber el largo de una tupla
print(len(first_tuple))

# Acceder a un elementos
print(first_tuple[2])

# Navegación inversa
print(first_tuple[-2])

# Acceder a un rango
print(first_tuple[0:2])
# A una tupla aunque solo sea un elemento al final se le debe agregar una coma

# Recorrer elementos
for frutas in first_tuple:
    print(first_tuple) # Es lo mismo que = 
    # Por default print tiene salto de línea, pero si queremos cambiarlo debemos hacer lo siguiente
    
for frutas in first_tuple:
    print(first_tuple,end=" ")
    
# Cambiar valor tupla
# first_tuple[0] = "Berenjena" | This will give us an error
frutalista = list(first_tuple)
frutalista[0] = "Berenjena"
print("\n",frutalista)


# Eliminar la tupla por completo
del first_tuple

# Dada la siguiente tupla, crear una lista que sólo incluya los números menor que 5 utilizando un ciclo for:

tupla33 = (13, 1, 8, 3, 2, 5, 8)
lista33 = []

for elemento in tupla33:
    if elemento < 5:
        lista33.append(elemento)

print(lista33)
