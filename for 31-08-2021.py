m = 5
for k in range(9,4,-1):
    m += k

print(m)

y = 3
iteraciones = 0
for i in range(4):
    y += 3
    iteraciones += 1

print(y)
print(iteraciones)

y = 2
iteraciones = 0
for i in range(2,8):
    y += i
    iteraciones += 1

print(y)
print(iteraciones)

suma = 3
iteraciones = 0
for j in range(2,8,3):
    suma *= j
    iteraciones += 1
print(suma)
print(iteraciones)

itera = 0
for letra in "Monterrey":
    itera += 1
print(itera)
print(letra)