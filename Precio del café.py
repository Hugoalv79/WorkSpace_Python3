# Prueba el siguiente código con un precio = 15,¿qué sucede? El programa repsonde con un "Está barato"
# Prueba el siguiente código con un precio = 30,¿qué sucede? El programa responde con un "Está bien"
# Prueba el siguiente código con un precio = 60,¿qué sucede? El programa responde con un "Está caro"


precio = int(input('Teclea el precio del café: '))

if precio < 25:
    print('Está barato') 
elif precio>=25 and precio<=50:
    print('Esta bien')
else:
    print('Esta caro')


#Da clic en Debug currente script, bicho verde
#Da clic en step into(F7) varias veces
#Corrige el código
#¿Cuál fue la utilidad del depurador en este caso? Ayuda a saber donde está el error

