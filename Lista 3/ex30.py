#Um comerciante comprou um produto e quer vendê-lo com um lucro de 45% se o valor da compra for menor que R$ 20,00 caso contrário, o lucro será de 30%. Faça um algoritmo e o fluxograma que leia o valor do produto e imprima o valor da venda.

valorCompra = float(input("Valor de compra: "))

if (valorCompra > 0 and valorCompra < 20):
    valorVenda = (valorCompra * 0.45) + valorCompra
    print(f"Valor de compra: {valorCompra:.2f}\nValor venda: {valorVenda:.2f}")
elif (valorCompra >= 20):
    valorVenda = (valorCompra * 0.30) + valorCompra
    print(f"Valor de compra: {valorCompra:.2f}\nValor Venda: {valorVenda:.2f}")
else:
    print("Valor de compra não pode ser negativo")