import pandas as pd
import matplotlib.pyplot as plt
from tabulate import tabulate
from time import *
import csv
import random

# LISTAS
lista_preguntas = []
examenes_realizados = []



# APERTURA DE ARCHIVOS/ ARCHIVOS A USAR
intentos = pd.read_csv("/content/Project Python/Intentos.csv")

with open("/content/Project Python/Lista_de_Preguntas.csv",encoding='windows-1252') as csv_file:
    csv_reader = csv.reader(csv_file)
    for line in csv_file:
        lista_preguntas.append(line.split(","))

for i in range(len(lista_preguntas)):
  lista_preguntas[i][-1] = lista_preguntas[i][-1].replace("\n", "")

with open("/content/Project Python/Examenes_Realizados.csv") as csv_file:
  csv_reader = csv.reader(csv_file)
  for line in csv_file:
    examenes_realizados.append(line.split(","))
for i in range(len(examenes_realizados)):
  examenes_realizados[i][-1] = examenes_realizados[i][-1].replace("\n", "")


# 1
def Registrar_pregunta():
    lista_incisos = []

    texto_pregunta = input("\nIngresa la nueva pregunta: ")
    incisos = ["a)","b)","c)","d)"]

    for i in range(4):
        Inciso = input(f"Ingresa el inciso {incisos[i]}: ")
        lista_incisos.append(Inciso)

    respuesta_correcta = int(input("""\nIngresa la respuesta correcta para evaluar
    1 --> Incizo a)
    2 --> Incizo b)
    3 --> Incizo c)
    4 --> Incizo d)
    """))

    # Revisar si el usuario escogió un una respuesta válida
    while respuesta_correcta < 1 or respuesta_correcta > 4:
        print("Ingresa un valor válido")
        respuesta_correcta = int(input("""¿Cuál es la respuesta correcta?
    1 --> el incizo a)
    2 --> el incizo b)
    3 --> el incizo c)
    4 --> el incizo d)
    """))

    # TODOS LOS INPUTS PROCESADOS
    lista_preguntas.append((str(f"{len(lista_preguntas) + 1} {texto_pregunta} {lista_incisos[0]} {lista_incisos[1]} {lista_incisos[2]} {incisos[3]} {respuesta_correcta}")).split())


    with open("Lista_de_Preguntas.csv", 'w') as csv_file_w:
        csv_writer = csv.writer(csv_file_w)
        for pregunta in lista_preguntas:
          csv_writer.writerow(pregunta)
    print("Pregunta resgistrada exitosamente")

#2
def Actualizar_pregunta():
    contador = 0
    print("\nPreguntas registradas:")
    for pregunta in lista_preguntas: #Aquí se imprimen las preguntas registradas y se pregunta cuál quieres actualizar
      contador += 1
      print(f"Pregunta {contador}: {pregunta}")
    pregunta_a_actualizar = int(input("\n¿Qué pregunta quiere modificar? (Ingrese el número): "))
    
    while pregunta_a_actualizar < 1 or pregunta_a_actualizar > len(lista_preguntas) + 1:
      print("Número inválido, inténtelo de nuevo porfavor")
      pregunta_a_actualizar = int(input("¿Qué pregunta quiere modificar? (Ingrese el número): "))
    
    print(f"\nNúmero de pregunta: {lista_preguntas[pregunta_a_actualizar - 1][0]}. "\
    f"Enfoque: {lista_preguntas[pregunta_a_actualizar - 1][1]}. "\
    f"Texto de la pregunta: {lista_preguntas[pregunta_a_actualizar - 1][2]}. "\
    f"Opción 1: {lista_preguntas[pregunta_a_actualizar - 1][3]}. "\
    f"Opción 2: {lista_preguntas[pregunta_a_actualizar - 1][4]}. "\
    f"Opción 3: {lista_preguntas[pregunta_a_actualizar - 1][5]}. "\
    f"Opción 4: {lista_preguntas[pregunta_a_actualizar - 1][6]}. "\
    f"Opción correcta: {lista_preguntas[pregunta_a_actualizar - 1][7]}")
    

    borrador_nueva_pregunta = ["", "", "", "", "", "", "", ""]

    print("Ingrese los datos nuevos, si no quiere actualizar el dato, presione 'enter'")

    borrador_nueva_pregunta[0] = lista_preguntas[pregunta_a_actualizar - 1][0]

    nuevo_enfoque = input("Nuevo enfoque: ")
    if nuevo_enfoque == "":
      borrador_nueva_pregunta[1] = lista_preguntas[pregunta_a_actualizar - 1][1]
    else:
      borrador_nueva_pregunta[1] = nuevo_enfoque

    nuevo_texto_pregunta = input("Nuevo texto de pregunta: ")
    if nuevo_texto_pregunta == "":
      borrador_nueva_pregunta[2] = lista_preguntas[pregunta_a_actualizar - 1][2]
    else:
      borrador_nueva_pregunta[2] = nuevo_texto_pregunta

    nueva_opcion1 = input("Ingresa una nueva opción 1: ")
    if nueva_opcion1 == "":
      borrador_nueva_pregunta[3] = lista_preguntas[pregunta_a_actualizar - 1][3]
    else:
      borrador_nueva_pregunta[3] = nueva_opcion1

    nueva_opcion2 = input("Ingresa una nueva opción 2: ")
    if nueva_opcion2 == "":
      borrador_nueva_pregunta[4] = lista_preguntas[pregunta_a_actualizar - 1][4]
    else:
      borrador_nueva_pregunta[4] = nueva_opcion2

    nueva_opcion3 = input("Ingresa una nueva opción 3: ")
    if nueva_opcion3 == "":
      borrador_nueva_pregunta[5] = lista_preguntas[pregunta_a_actualizar - 1][5]
    else:
      borrador_nueva_pregunta[5] = nueva_opcion3

    nueva_opcion4 = input("Ingresa una nueva opción 4: ")
    if nueva_opcion4 == "":
      borrador_nueva_pregunta[6] = lista_preguntas[pregunta_a_actualizar - 1][6]
    else:
      borrador_nueva_pregunta[6] = nueva_opcion4

    nueva_respuesta_correcta = input("Ingrese una nueva respuesta correcta: ")
    if nueva_respuesta_correcta == "":
      borrador_nueva_pregunta[7] = lista_preguntas[pregunta_a_actualizar - 1][7]
    else:
      borrador_nueva_pregunta[7] = nueva_respuesta_correcta

    print("Así quedaría la nueva opción: ")

    print(f"\nNúmero de pregunta: {borrador_nueva_pregunta[0]}. "\
    f"Enfoque: {borrador_nueva_pregunta[1]}. "\
    f"Texto de la pregunta: {borrador_nueva_pregunta[2]}. "\
    f"Opción 1: {borrador_nueva_pregunta[3]}. "\
    f"Opción 2: {borrador_nueva_pregunta[4]}. "\
    f"Opción 3: {borrador_nueva_pregunta[5]}. "\
    f"Opción 4: {borrador_nueva_pregunta[6]}. "\
    f"Opción correcta: {borrador_nueva_pregunta[7]}")
    cambiar_pregunta = input("¿Está seguro de que quiere actualizar los datos de la pregunta? (1-sí 2-no)")

    while cambiar_pregunta != "1" and cambiar_pregunta != "2":
      print("Inválido, inténtelo otra vez")
      cambiar_pregunta = input("¿Está seguro de que quiere actualizar los datos de la pregunta? (1-sí 2-no)")

    if cambiar_pregunta == "1":
      lista_preguntas[pregunta_a_actualizar - 1] = borrador_nueva_pregunta
        
      with open("Lista_de_Preguntas.csv", 'w') as csv_file_w:
        csv_writer = csv.writer(csv_file_w)
        for pregunta in lista_preguntas:
          csv_writer.writerow(pregunta)

      print("Pregunta actualizada con éxito")

#3
def EvaluacionLectura(Nombre,Apellidos):
    print(f"""
    EVALUACIÓN DE LA COMPRENSIÓN LECTORA
    A continuación se te presentarán una serie de preguntas, recuerda que una vez decidas pasar a la siguiente no podrás regresar, no hay límite de tiempo para responder""")
   
    lista_preguntas_posibles_lectura = []

    for pregunta in range(len(lista_preguntas)):
      if lista_preguntas[pregunta][1] == "Lectura":
        lista_preguntas_posibles_lectura.append(lista_preguntas[pregunta])
     
    diez_preguntas_lectura = []
   
    random_questions_lectura = random.sample(range(len(lista_preguntas_posibles_lectura)), 10)
    
    for pregunta in range(len(random_questions_lectura)):
      diez_preguntas_lectura.append(lista_preguntas_posibles_lectura[random_questions_lectura[pregunta]])
   
    print("\nLectura:")
    aciertos_lectura, errores_lectura = Hacer_pregunta(diez_preguntas_lectura, random_questions_lectura)
    
    print(f"Lecturas: \nAciertos: {aciertos_lectura} - Errores: {errores_lectura}")
    

    total_aciertos = aciertos_lectura
    total_errores = errores_lectura
    calif = (total_aciertos / 10) * 100

    pregunta_realizada = f"{len(examenes_realizados) + 1},{calif},{total_aciertos},{total_errores}"
    examenes_realizados.append(pregunta_realizada.split(","))

    with open("Examenes_Realizados.csv", 'w') as csv_file_w:
        csv_writer = csv.writer(csv_file_w)
        for examen in examenes_realizados:
          csv_writer.writerow(examen)

    #Poner un tiempo de 20 minutos

#4
def Reportar_calificaciones():

    suma_califs = 0
    for examen in range(len(examenes_realizados)):
      suma_califs += round(float(examenes_realizados[examen][1]))
    suma_aciertos = 0
    for examen in range(len(examenes_realizados)):
      suma_aciertos += round(float(examenes_realizados[examen][2]))
    suma_errores = 0
    for examen in range(len(examenes_realizados)):
      suma_errores += round(float(examenes_realizados[examen][3]))

    promedio_califs = "{:.2f}".format(suma_califs/len(examenes_realizados))
    porcentaje_aciertos = "{:.2f}".format((suma_aciertos/(10*len(examenes_realizados)))*100)
    porcentaje_errores = "{:.2f}".format((suma_errores/(10*len(examenes_realizados)))*100)

    
    Tabla = {'Headers': ["Examenes realizados", 
                         "Promedio de calificaciones", 
                         "Preguntas correctas", 
                         "Preguntas incorrectas"],
             'Datos': [len(examenes_realizados), 
                       promedio_califs, 
                       f"{porcentaje_aciertos}%", 
                       f"{porcentaje_errores}%"]}
        
    print(tabulate(Tabla, tablefmt='fancy_grid'))

# AUX
def Hacer_pregunta(posibles_preguntas, orden):
    Aciertos = 0
    Errores = 0
    for i in range(len(orden)):
      print(f"\nPregunta {i + 1}: {posibles_preguntas[orden[i]][2]}")
      print(f"A) {posibles_preguntas[orden[i]][3]}")
      print(f"B) {posibles_preguntas[orden[i]][4]}")
      print(f"C) {posibles_preguntas[orden[i]][5]}")
      print(f"D) {posibles_preguntas[orden[i]][6]}")

      respuesta = input("Respuesta: ")
      respuesta.lowecase()
      if respuesta == posibles_preguntas[orden[i]][7]:
        Aciertos += 1
      else:
        Errores += 1

    return Aciertos, Errores


######################################################################################

print("""BIENVENID@ A TU HERRAMIENTA DE APRENDIZAJE""")
# DATOS DE USUARIO
Nombre=input("Ingresa tu nombre(s): ")
Apellidos=input("Ingresa tus apellidos: ")

 # Imprime el menu y realiza una función dependiendo el input
while True:
    print("""
    Menu:
    
    1. Evaluación de Lectura
    2. Reporte de calificaciones
    3. Agregar pregunta
    4. Modificar pregunta
    5. Salir 
    """)
    opcion = input("Elige una opción: ")

    if opcion == "1":
        EvaluacionLectura(Nombre,Apellidos)
        

    elif opcion == "2":
        Reportar_calificaciones()
        

    elif opcion == "3":
        Registrar_pregunta()
        

    elif opcion == "4":
        Actualizar_pregunta()
        

    elif opcion == "5":
        print("¡Nunca pares de aprender!")
        break

    else:
        print("No se reconoce la opción") 