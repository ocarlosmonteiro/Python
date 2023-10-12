import math

x1 = int(input("Informe as coordenadas de X1: "))
y1 = int(input("Informe as coordenadas de Y1: "))
x2 = int(input("Informe as coordenadas de X2: "))
y2 = int(input("Informe as coordenadas de Y2: "))

r = math.sqrt ((x2 - x1) * (x2 -x1) + (y2 - y1) * (y2 - y1))

print ("Coordenada é : ", r)