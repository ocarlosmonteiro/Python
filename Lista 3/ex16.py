#Faça um algoritmo e o fluxograma que leia dois números e exiba se o primeiro é divisível pelo segundo.

n1 = int(input("Digite um número: "))
n2 = int(input("Digite outro número: "))

d = n1 / n2

if (n1 % n2 == 0):
    print(f"{n1:.0f} é divisivel por {n2:.0f}")
else:
    print(f"{n1:.0f} não é divisevel por {n2:.0f}")