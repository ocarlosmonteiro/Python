#Faça um algoritmo e o fluxograma que leia o salário de uma pessoa e imprima o desconto do INSS segundo a tabela abaixo:
#Faixa                                                  | Desconto
#Menor ou igual a R$ 600,00                             | isento
#Maior que R$ 600,00 e menor ou igual a R$ 1200,00      | 20%
#Maior que R$ 1200,00 e menor ou igual a R$ 2000,00     | 25%
#Maior que R$ 2000,00                                   | 30%

salario = float(input("Digite o salário: "))

if (salario >0 and salario <= 600):
    print("Isento de desconto.")
elif (salario > 600 and salario <=1200):
    desconto = salario * 0.20
    salarioDesconto = salario - desconto
    print(f"Salário: {salario:.2f}\nDesconto: {desconto:.2f}\nSalário com desconto: {salarioDesconto:.2f}")
elif (salario > 1200 and salario <= 2000):
    desconto = salario * 0.25
    salarioDesconto = salario - desconto
    print(f"Salário: {salario:.2f}\nDesconto: {desconto:.2f}\nSalário com desconto: {salarioDesconto:.2f}")
elif (salario > 2000):
    desconto = salario * 0.30
    salarioDesconto = salario - desconto
    print(f"Salário: {salario:.2f}\nDesconto: {desconto:.2f}\nSalário com desconto: {salarioDesconto:.2f}")
else:
    print("Salário tem que ser positivo")