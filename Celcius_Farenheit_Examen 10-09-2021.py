# A00834109 Hugo Tonatiuh Alvarado Garcia
# LIBERÍAS A USAR
from random import *

# DECLARACION DE VARIABLES
a = uniform(40,50)
a = round(a,1)

b = uniform(90,100)
b = round(b,1)

# BLOQUE
print("TABLA DE CONVERSIÓN DE C° A F° Y F° A C°")
for i in range(0,10):
    far = (a*1.8)+32
    far =round(far,1)
    cel = (b-32)/1.8
    cel = round(cel,1)
    print(a,"C°"," = ",far,"F°"," y ",b,"F°"," = ",cel,"C°")
    a-= 1
    b-= 1

