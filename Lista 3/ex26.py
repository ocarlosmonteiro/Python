#Faça um algoritmo e o fluxograma que leia três números e imprima-os em ordem decrescente (suponha números diferentes).

a = float(input("Digite um número: "))
b = float(input("Digite um número: "))
c = float(input("Digite um número: "))

if (a < b and a < c and b < c):
    menor = a
    inter = b
    maior = c
    print(maior, inter, menor)
elif (a < b and a < c and c < b):
    menor = a
    inter = c
    maior = b
    print(maior, inter, menor)
elif (b < a and b < c and a < c):
    menor = b
    inter = a
    maior = c
    print(maior, inter, menor)
elif (b < a and b < c and c < a):
    menor = b
    inter = c
    maior = a
    print(maior, inter, menor)
elif (c < a and c < b and a < b):
    menor = c
    inter = a
    maior = b
    print(maior, inter, menor)
else:
    menor = c
    inter = b
    maior = a