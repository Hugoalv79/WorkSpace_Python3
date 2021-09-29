from math import pi

print("                                   AREA AND VOLUME CALCULATOR OF A CYLINDER   ")

r = float(input("Enter the value of radio(r): "))
h = float(input("Enter the value of height(h): "))

Area = 2*pi*r*(h+r)
Area = round(Area,3)

Volumen = pi*(r**2)*h
Volumen = round(Volumen,3)

print(f"""            RESULTS
            The Area is: {Area}
            The Volumen is: {Volumen}
      """)