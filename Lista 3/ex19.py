#Faça um algoritmo e o fluxograma que leia dois números e imprima uma mensagem dizendo se são iguais ou diferentes.

n1 = float(input("Digite um número: "))
n2 = float(input("Digire outro número: "))

if (n1 > n2):
    print(n1)
elif (n2 > n1):
    print(n2)
else:
    print("Números são iguais")