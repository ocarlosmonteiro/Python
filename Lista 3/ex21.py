#Faça um algoritmo e o fluxograma que leia dois números e imprima-os em ordem crescente (suponha números diferentes).

n1 = float(input("Digite um número: "))
n2 = float(input("Digite outro número: "))

if (n1 > n2):
    print(n2, n1)
elif (n2 > n1):
    print(n1, n2)
else:
    print("Números são iguais")