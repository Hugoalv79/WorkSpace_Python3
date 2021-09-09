#Da clic en Debug currente script, bicho verde
#Da clic en step into(F7) varias veces
#¿Qué debemos hacer para corregir el código? Hacía falta convertir al final las variables a número para que
# pudiera seguir haciendo las comparaciones de mayor que
# Escribe el código faltante
for hora in range(24):
    for minuto in range(60):
        for segundo in range(60):
            if hora <10:
                hora = '0' + str(hora)
            if minuto <10:
                minuto = '0' + str(minuto)
            if segundo <10:
                segundo = '0' + str(segundo)
            print(hora,minuto,segundo,sep=':')
            hora = int(hora)
            minuto = int(minuto)
            segundo = int(segundo)