

# DECLARACION DE FUNCIONES
def feet_cm(valor):
    return valor * 30.48
def pul__cm(valor):
    return valor * 2.54
def yard_cm(valor):
    return valor * 91.44

# BIENVENIDA A USUARIO
print("""CONVERSOR A CM
      1°- Pies a cm
      2°- Pulgadas a cm
      3°- Yardas a cm
      """)
x = int(input("¿Qué desea convertir? "))
valor = float(input("Ingrese las unidades a convertir: "))

if 1<= x and x<4:
    if x == 1:
        if valor<=0:
            print("Error")
        else:
            print(feet_cm(valor))
        exit()
        
    elif x == 2:
        if valor<=0:
            print("Error")
        else:
            print(pul__cm(valor))
        exit()
        
    elif x == 3:
        if valor<=0:
            print("Error")
        else: 
            print(yard_cm(valor))
        exit()
        
else:
    print("Error")

