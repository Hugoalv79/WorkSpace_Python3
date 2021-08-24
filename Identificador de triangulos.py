#                                          IDENTIFICADOR DE TRIANGULOS
#  Escribe un programa que dados 3 números enteros, que representan la longitud de los lados de un triángulo, 
#  muestre en la pantalla el tipo de triángulo de que se trata (equilátero, isósceles o escaleno).
#  Considera que X, Y y Z son los lados de un triángulo si cumplen con las siguientes condiciones:

#   Todos los números deben ser mayores que cero
#  * X + Y > Z
#  * X + Z > Y
#  * Y + Z > X


# es decir, la suma de dos de las medidas debe ser estrictamente mayor que la tercera.


# Recuerda que el triángulo equilátero tiene 3 lados iguales, el isósceles tiene 2 lados iguales y el escaleno 
# tiene los 3 lados diferentes.)
print("""                                  IDENTIFICADOR DE TRIANGULOS
Las medidas ingresadas deben de cumplir con las siguientes condiciones:
   Todos los números deben ser mayores que cero
  * X + Y > Z
  * X + Z > Y
  * Y + Z > X
""")

primer_lado = float(input("Ingresa la medida del primer lado: "))
segundo_lado = float(input("Ingresa la medida del segundo lago: "))
tercer_lado = float(input("Ingresa la medida del terccer lado: "))

if primer_lado > 0 and segundo_lado > 0 and tercer_lado > 0 and (primer_lado + segundo_lado) > tercer_lado and (primer_lado + tercer_lado) > segundo_lado and (segundo_lado + tercer_lado) > primer_lado:
    if primer_lado == segundo_lado and segundo_lado == tercer_lado:
        print("Es un triángulo equilatero")
    elif primer_lado == segundo_lado or segundo_lado == tercer_lado or primer_lado == tercer_lado:
        print("Es un triágulo isóceles")
    elif primer_lado != segundo_lado and segundo_lado != tercer_lado:
        print("Es un triángulo escaleno")

else:
    print("Las medidas de los lados no cumplen los requisitos")