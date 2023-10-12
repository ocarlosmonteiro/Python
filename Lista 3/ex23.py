#Faça um algoritmo e o fluxograma que leia três números e imprima o maior número (suponha números diferentes).

n1 = float(input("Digite um número: "))
n2 = float(input("Digite um número: "))
n3 = float(input("Digite um número: "))

if (n1 > n2 and n1 > n3):
    print(f"N1: {n1:.1f}")
elif (n2 > n1 and n2 > n3):
    print(f"N2: {n2:.1f}")
elif (n3 > n1 and n3 > n2):
    print(f"N3: {n3:.1f}")
else:
    print("Números são iguais")