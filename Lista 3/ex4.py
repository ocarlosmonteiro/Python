#Desenvolva um algoritmo e o fluxograma que:
# - Leia 4 (quatro) números;
# - Calcule o quadrado de cada um;
# - Se o valor resultante do quadrado do terceiro for >= 1000, imprima-o e finalize;
# - Caso contrário, imprima os valores lidos e seus respectivos quadrados.

n1 = float(input("nforme um número: "))
n2 = float(input("nforme um número: "))
n3 = float(input("nforme um número: "))
n4 = float(input("nforme um número: "))

qn1 = n1 * n1
qn2 = n2 * n2
qn3 = n3 * n3
qn4 = n4 * n4

if (qn3 > 1000):
    print(f"Quandro de N3 é: {qn3}")
else:
    print(f"Valor informado de N1: {n1}, seu quadrado: {qn1}\nVAlor informado de N2: {n2}, seu quadrado é: {qn2}\nValor informado de N3: {n3}, seu quadrado é: {qn3}\nValor informado de N4: {n4}, seu quadrado é: {qn4}")