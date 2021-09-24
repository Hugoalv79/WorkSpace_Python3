
# FUNCIONES
def primera(primer_valor, segundo_valor, clave):
    if clave == "s":
        return primer_valor+segundo_valor
        exit()
        
    if clave == "r":
        return primer_valor-segundo_valor
        exit()
        
    if clave =="m":
        return primer_valor*segundo_valor
        exit()
        
    if clave =="d":
        return primer_valor/segundo_valor
        exit()
          

def segunda():
    primer_valor = -1
    segundo_valor = -1
    while primer_valor<0 or segundo_valor<0:
        primer_valor = float(input("Introduce un valor: "))
        segundo_valor = float(input("Introduce el segundo valor: "))
        if primer_valor or segundo_valor <0:
            print("Solo números positivos")
    
    print("""
      CLAVE      SIGNIFICADO
         s         Suma
         r         Resta
         m         Multiplicación
         d         División  
      """)
    
    clave = "x"
    while clave not in ['s', 'r',"m","d"]:
        clave = input("Selecciona la clave de la operación que deseas hacer: ")
        if clave not in ['s', 'r',"m","d"]:
            print("Introduzca una clave válida")


    print(primera(primer_valor, segundo_valor, clave))
    
# clave != "s" and clave!="r" and clave!="m" and clave!="d":
# while f_l.lower() not in ['s', 'q']:
# clave not in ['s', 'r',"m","d"]:
       
# EJECUCIÓN 
segunda()
    
