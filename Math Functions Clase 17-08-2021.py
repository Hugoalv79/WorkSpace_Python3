from math import pi, sqrt, ceil
print(pi)
    
# random.random():

#random.uniform

#a = pi * 20
# print("Rel resultado es: ", pi)
print("""-----------------------------------------EJERCICIO--------------------------------------------------
El área y el volumen de una esfera se calcula con las siguientes fórmulas:
A = 4PiR**2
Volumen = 4Pir**3/3""")

radio = float(input("Cuanto vale el radio?: "))
area = 4 * pi * (radio**2)
volumen = (4 * pi * radio**3) / 3

print("El valor del área es: "+ str(round(area,2)))
print("El valor del volumen es: "+ str(round(volumen,2)))

print("""-------------------------------------------EJERCICIO 2 ----------------------------------------------

""")

a = float(input("Cuál es el valor del primer lado?: "))
b = float(input("Cuál es el valor del segundo lado?: "))
c = float(input("Cuál es el valor del tercer lado?: "))

s = (a + b + c) / 2
area_triangulo = round(sqrt(s*(s - a)*(s - b)*(s - c)), 3)

print("El área del triangulo es: "+ str(area_triangulo))

print("""------------------------------------EJERCICIO 3-------------------------------------------------
Escribe un programa que imprimia un numero aleatorio entre 0 y 1(float), y que también imprima un número
entero entre 1 y 10""")

print("""------------------------------------EJERCICIO 4----------------------------------------------------
 Escribe un programa que te permita encontrar el entero inmediato superior de los siguientes números:
 1°- 4.7823
 2°- 2.459
 3°- 16.385  
""")

num1 = 4.7823
num2 = 2.459
num3= 16.385

topnum1 = ceil(num1)
topnum2 = ceil(num2)
topnum3 = ceil(num3)

print("El numero inmediato superior de " + str(num1) + " es:" + str(topnum1))
print("El numero inmediato superior de " + str(num2) + " es:" + str(topnum2))
print("El numero inmediato superior de " + str(num3) + " es:" + str(topnum3))