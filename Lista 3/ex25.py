#Faça um algoritmo e o fluxograma que leia três números e imprima-os em ordem crescente (suponha números diferentes).

a = float(input("Digite um número: "))
b = float(input("Digite um número: "))
c = float(input("Digite um número: "))

if (a > b and a > c and b > c):
    maior = a
    inter = b
    menor = c
    print(menor, inter, maior)
if (a > b and a > c and c > b):
    maior = a
    inter = c
    menor = b
    print(menor, inter, maior)
elif (b > a and b > c and a > c):
    maior = b
    inter = a
    menor = c
    print(menor, inter, maior)
elif (b > a and b > c and c > a):
    maior = b
    inter = c
    menor = a
    print(menor, inter, maior)
elif (c > a and c > b and a > b):
    maior = c
    inter = a
    menor = b
    print(menor, inter, maior)
elif (c > a and c > b and b > a):
    maior = c
    inter = b
    menor = a
    print(menor, inter, maior)