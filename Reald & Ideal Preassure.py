print('Ingresa Volumen(L')
V=float(input())
print()

print('Moles(n)')
n=float(input())
print()

print('Temperature(Kelvin)')
T=float(input())
print()

print('a')
a=float(input())
print()

print('b')
b=float(input())
print()

R=0.08206
Pi=(n*R*T)/V
Pr=((n*R*T)/(V-(n*b)))-((a*(n**2))/(V**2))
8
print('Presión Ideal: '+str(Pi))
print('Presión Real: '+str(Pr))
print()
print('Diferencia de Presión: '+ str(Pi-Pr))
