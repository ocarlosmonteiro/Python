#Faça um algoritmo e o fluxograma que leia dois números e imprima o menor número (suponha números diferentes).

n1 = float(input("Digite um núemro: "))
n2 = float(input("Digite ouotro número: "))

if (n1 < n2):
    print(n1)
elif (n2 < n1):
    print(n2)
else:
    print("Números são iguais")