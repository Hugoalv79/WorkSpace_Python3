from random import *

aleatorio = randint(5,15)
respuesta = -10

while aleatorio != respuesta:
    respuesta = int(input("Ingresa un número: "))

    if aleatorio != respuesta:
        print("Intenta de nuevo ")
    
    elif aleatorio == respuesta:
        print("Felicidades, le atinaste al número")

print("El número aleatorio era: ",str(aleatorio))

