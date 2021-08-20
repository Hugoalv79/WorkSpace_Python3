print("Introducir 3 números diferentes")
a = int(input("Escribe el número 1: "))
b = int(input("Escribe el número 2: "))
c = int(input("Escribe el número 3: "))

if a > b and a > c and b > c:
    print("\n",a,"\n",b,"\n",c)

if a > c and a > b and c > b:
    print("\n",a,"\n",c,"\n",b)

if b > a and b > c and a > c:
    print("\n",b,"\n",a,"\n",c)

if b > c and b > a and c > a:
    print("\n",b,"\n",c,"\n",a)