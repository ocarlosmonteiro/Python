#Faça um algoritmo e o fluxograma que leia um número inteiro e mostre uma mensagem indicando se este número é par ou ímpar, e se é positivo ou negativo.

n = int(input("Informe um nnúmero: "))

r = n % 2 

if (r == 0):
    print(f"{n:.0f} é par!")
else:
    print(f"{n:.0f} é impar!")