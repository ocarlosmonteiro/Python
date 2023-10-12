#Faça um programa que entre com o saldo e aplique um percentual de 10%. Mostre o valor com o reajuste.

valor = float(input("Informe o valor: "))

reajuste = valor * 0.10

valorReajustado = valor + reajuste

print(f"Valor reajustado é {valorReajustado:.2f}\nValor do reajuste é: {reajuste}")