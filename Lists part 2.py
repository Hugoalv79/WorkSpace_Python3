nombres = ["Juan", "Karla", "Ricardo","María"]

# Imprimir la lista nombres
print(nombres)

# Acceder a los valores de una lista
print(nombres[0])
print(nombres[1])

# Acceder a los elemenos de manera inversa
print(nombres[-1])
print(nombres[-2])

# Imprimir un rango
print(nombres[0:2]) # Sin incluir el índice dos

# Ir del inicio de la lista al inidice(Sin incluirlo)
print(nombres[:3])

# Desde el incide indicado hasta el final
print(nombres[1:])

# Cambiar un valo
print(nombres)
nombres[3] = "Ivone"
print(nombres)

for nombre in nombres:
    print(nombre)
else:
    print("No existen más nombres en la lista")
    
# Preguntar el largo de una lista
print(len(nombres))
#                                            INSERTAR
# Agregar a la lista
nombres.append("Lorenso")
print(nombres)

# Insertar un elemento en un ídnice en específico
nombres.insert(1,"Octavio")
print(nombres)
#                                            REMOVER
# Remover un elemento
nombres.remove("Octavio")
print(nombres)

# Remover el último valor agregado
nombres.pop()
print(nombres)

# Remover un elemento en un índice determitado
del nombres[0]
print(nombres)

# Limpiar la lista
nombres.clear()
print(nombres)

# Borrar la lista por completo
del nombres  # < Esto elimina la existencia de la lista
# print(nombres)

for i in range(1,10):
    if i % 3 == 0:
        print(i)