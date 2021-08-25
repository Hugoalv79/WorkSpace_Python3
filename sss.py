# Dos formas para hacer ciclos:
#  while     for
# COMPARACIÓN
# ==  igual a
# > mayor que    
# < menor que  
# != significa que no es igual

# While se usa cuando no sabes cuantas veces tienes que repetir algo, y además tienes que poner una condición
# de fin

# jugos = 0

# while jugos < 15:
#     print(jugos)
#     jugos = jugos + 1

# LIBRERIAS A UTILIZAR
from datetime import datetime

# VARIABLES
today = datetime.now()
today = str(today)
mes_now =  today[5:7]# Saber el mes actual
mes_now = int(mes_now) # El número del mes actual
no_depositos = int(input("¿Cuántos depósitos son en total: ")) # Numero de depositos
i = int(0)
importes_correctos = int(0)
total_de_importes = float(0) # Valor de dinero de todos los importes sumados
# ESTRUCTURA DEL CÓDIGO

while i < no_depositos:
    # Se ingresan los datos del importe
    user_mes_importe_recibido = input("Ingresa los datos del importe: ")
    user_mes_importe_recibido = user_mes_importe_recibido.split(",")
    no_mes_importe = int(user_mes_importe_recibido[0]) # Número de mes del importe

    if mes_now == no_mes_importe: # Verificar si el mes del importe coincide con el mes actual
        user_valor_importe = user_mes_importe_recibido[1] # El valor del importe es igual al monto registrado 
        user_valor_importe = float(user_valor_importe)
    # por el usuario
        importes_correctos += 1
        total_de_importes = total_de_importes + user_valor_importe
        i += 1
    else:
       i += 1

print("""TOTAL DE $ EN IMPORTES
         $""", str(total_de_importes))
print("Total de importes del mes en curso: ", str(importes_correctos))
