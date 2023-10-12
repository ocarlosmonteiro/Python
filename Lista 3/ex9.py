#Faça um algoritmo e o fluxograma que leia um número e informe se ele é ou não divisível por 5.

n = int(input("Digite  um número: "))

d = n % 5

if (d == 0):
    print(f"{n:.0f} é divisivel por 5")
else:
    print(f"{n:.0f} não é divisivel por 5")