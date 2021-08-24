determination = int(input())

if determination % 2 == 0:
    par = True
else:
    par = False



if par:
    if determination >= 0:
        print("El número es par positivo")
    elif determination < 0:
        print("El número es par negativo")
    else:
        None
elif par == False:
    if determination >= 0:
        print("El número es impar positivo")
    elif determination <0:
        print("El número es impar negativo")
else: None