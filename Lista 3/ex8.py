#Faça um algoritmo e o fluxograma que leia dois valores numéricos e efetue a adição, caso o resultado seja maior que 10 apresentá-lo.

n1 = float(input("Digite um número: "))
n2 = float(input("Digite outro número: "))

ad = n1 + n2

if (ad > 10):
    print(f"{ad:.0f}")
else:
    print("Número menor que 10.")