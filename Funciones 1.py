# Crear una función para sumar los valores recibidos de tipo numérico, utilizando argumentos variables *args como parámetro de la función y 
# regresar como resultado la suma de todos los valores pasados como argumentos.

# Questions for this assignment
# ¿Cuál es el código de la función?

#Definición de la función para sumar valores
def plus_values(*args):
    resultado = 0
    for valor in args:
        resultado += valor
    return resultado

#LLamada de la función
print(plus_values(3,5,9))

print("-"*150)

# def listarTerminos(**kwargsOTerminos):
    
def desplegar_nombres(nombres):
    for nombre in nombres:
        print(nombre)
        
nombres = ["Juan Villalvazo","Karla Monther","María Magdalena","Juanalacubana"]
desplegar_nombres(nombres)
print("-"*150)
desplegar_nombres("Carlos Sedas")
print("-"*150)
# desplegar_nombres(10) # No va a funcionar esta
# desplegar_nombres(10,11) # No va a funcionar esta
desplegar_nombres((10,11)) # Tuplas
print("-"*150)
desplegar_nombres([8,9]) # Lista
print("-"*150)
print("""                                                                FUNCIONES RECURSIVAS
      Son funciones que se mandan a llamar a sí mismas hasta que el objetivo esté completado.
      Como ejemplo de esto tenemos el cálculo de un número factorial
      """)
def factorial(numero):
    if numero == 1:
        return 1
    else:
        return numero * factorial(numero-1)
    
numero = 7    
resultado = factorial(numero)
print(f"El factorial de {numero} es {resultado}")
print("-"*150)
print("""                                                                ASSIGMENT RECURSIVE FUNCTION

Imprimir numeros de 5 a 1 de manera descendente usando funciones recursivas. Puede ser cualquier valor positivo, ejemplo, si pasamos el valor 
de 5, debe imprimir: 5 4 3 2 1 Si se pasa el valor de 3, debe imprimir: 3 2 1 Si se pasan valores negativos no imprime nada""")

def imprimir_numero_recursivo(numerox):
    if numerox >= 1:
        print(numerox)
        imprimir_numero_recursivo(numerox-1)

imprimir_numero_recursivo(5)