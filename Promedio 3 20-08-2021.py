print("Ingresa tus calificaciones")
Mate = float(input("Ingresa calificación de Matemáticas: "))
Programacion = float(input("Ingresa calificación de Programación: "))
Fisica = float(input("Ingresa calificación de Física: "))

if Mate > 0 and Programacion > 0 and Fisica > 0 and Mate < 101 and Programacion < 101 and Fisica < 101:
    Promedio = (Mate + Programacion + Fisica) / (3)
    if Promedio >= 70:
        print("Aprobado con {:.2f} de promedio".format(Promedio))
    elif Promedio < 70:
        print("Reprobado con {:.2f} de promedio ".format(Promedio))
else:
    print("Carácteres no válidos")