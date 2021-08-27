print("                                                     EJERCICIO 1")
print(""" Realiza un script en Python que dada una longitud en metros, calcule y muestre su equivalente en pies.
# Recuerda que 1 pie = 12 pulgadas, 1 pulgada = 2.54 cm, 1 m = 100 cm
# Se debe pedir al usuario que introduzca el valor de la longitud.
# Se debe imprimir el valor de pies redondeado a dos dígitos
# Entrada
# 1
# Salida
# 1 metros es = 3.28 pies """)

metros = float(input("Introduce los metros: "))
pies = (metros * 100) / (2.54 * 12)
print( str(metros) + " metros es igual a " + str(round(pies, 2)) + " pies")

print("                                                     EJERCICIO 2")
print("""Realiza un script en Python que pida 3 valores, al final te muestre el mayor y el menor de ellos.
# Los 3 datos se deben pedir al usuario.
# Utiliza la funciones min() y max(). """)
 
# Entrada 
# 3
# 6
# 2
# Salida
# El numero mayor es = 6
# El número menor es = 2

a = float(input("Introduce el primer valor: "))
b = float(input("Introduce el segundo valor: "))
c = float(input("Introduce el tercer valor: "))

Valor_maximo = max(a,b,c)
Valor_minimo = min(a,b,c)
print("El valor máximo es: " + str(Valor_maximo))
print("El valor mínimo es: " + str(Valor_minimo))

print("                                                 EJERCICIO 3")
print("""Realiza un script en Python que pida un número entero y regrese su correspondiente carácter, el 
anterior y el siguiente. Ejemplo se ingresa 64 y se imprime 63 = '?', 64 = '@' y 65 = 'A'
# Entrada 
# 64
# Salida 
# 63 = '?'
# 64 = '@'
# 65 = 'A'.
 Recuerda que para encontrar algunas funciones que te ayuden a realizar algunos de los ejercicios debes revisar 
 en la siguiente página """)

Movimiento = int(input("Escribe un numero entero: "))
Alfa = chr(Movimiento - 1)
Beta = chr(Movimiento)
Gamma = chr(Movimiento + 1)

print(Alfa)
print(Beta)
print(Gamma)
