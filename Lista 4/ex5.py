# O cardápio de uma lancheria é o seguinte:

# Especificação    | Código | Preço
# Cachorro quente  |  100   | 3.20
# Bauru simples    |  101   | 3.30
# Bauru com ovo    |  102   | 3.50
# Hambúrguer       |  103   | 4.20
# Cheeseburguer    |  104   | 5.30
# Refrigerante     |  105   | 3.00

# Implemente um programa que leia o código do item pedido, a quantidade e calcule o valor a ser pago por aquele lanche. Considere que a cada execução somente será calculado um item. Use o comando switch.

codigo = int(input("Código do produto: "))
while (codigo < 100 or codigo > 105):
    print("Código invalido")
    codigo = int(input("Código do produto: "))

match codigo:
    case 100:
        preco = 3.20
        print(f"Código: {codigo:.0f} | Especificação: Cachorro quente | Preço: {preco:.2f}")
    case 101:
        preco = 3.30
        print(f"Código: {codigo:.0f} | Especificação: Bauru simples | Preço: {preco:.2f}")
    case 102:
        preco = 3.50
        print(f"Código: {codigo:.0f} | Especificação: Bauru com ovo | Preço: {preco:.2f}")
    case 103:
        preco = 4.20
        print(f"Código: {codigo:.0f} | Especificação: Hambúrguer | Preço: {preco:.2f}")
    case 104:
        preco = 5.30
        print(f"Código: {codigo:.0f} | Especificação: Cheeseburguer | Preço: {preco:.2f}")
    case 105:
        preco = 3.00
        print(f"Código: {codigo:.0f} | Especificação: Refrigerante | Preço: {preco:.2f}")

quantidade = int(input("Quantidade: "))

valor_pagar = preco * quantidade

print(f"Código: {codigo:.0f}\nPreço unitário: {preco:.2f}\nValor a pagar: {valor_pagar:.2f}")