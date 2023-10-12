#Crie um programa que leia quatro números do teclado e imprima a média deles na tela.

n1 = float(input("Informe um número: "))
n2 = float(input("Informe outro número: "))
n3 = float(input("Informe outro número: "))
n4 = float(input("informe outro número: "))

m = (n1 + n2 +n3 +n4)/4

print(f"Média dos núemros é: {m:.1f}")