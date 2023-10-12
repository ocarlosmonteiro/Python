#Dados dois lados de um triângulo retângulo, faça um programa para calcular a hipotenusa.
import math
a = int(input("Informe cateto oposto: "))
b = int(input("Informe cateto adjacente: "))
c = math.sqrt((a ** 2) + (b ** 2))
print(f"Hipotenusa é igual a: {c}")