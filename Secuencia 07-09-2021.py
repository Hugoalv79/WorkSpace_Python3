#                                                EJERCICIO EN CLASE
# Considere que toma como entrada un entero positivo n.
# El valor n no debe ser menor a 1 y tampoco mayor que 10
# Si n es par, el algoritmo lo divide por dos, y si n es impar, el algoritmo lo multiplica por tres y suma uno.
# El algoritmo repite esto, hasta que n es uno.

# Por ejemplo, la secuencia para n = 3 es la siguiente.

# 3-10-5-16-8-4-2-1

# Todos los números deben aparecer en un solo renglón deben estar separados por guiones.

n = int(input("Ingresa un número: "))
print(n,end="-")
if n >= 1 and n < 10:
    while n != 1:
        if n % 2 == 0:
            n = n/2
            n = int(n)
            print(n,end="-")   
        elif n % 2 != 0:
            n = (n * 3) + 1
            n = int(n)
            print(n,end="-")
else:
    pass
