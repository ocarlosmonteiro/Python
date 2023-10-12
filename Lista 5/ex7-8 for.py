#Uma fábrica tem 10 representantes. Cada um recebe uma comissão calculada a partir do número de itens de um pedido, segundo os seguintes critérios:
#- para menos de 20 itens vendidos, a comissão é de 10% do valor total do pedido;
#- para pedidos de 20 e 49 itens, a comissão é de 15% do valor total do pedido;
#- para pedidos de 50 a 74 itens, a comissão é de 20% do valor total do pedido; e
#- para pedidos iguais ou superiores, a 75 itens a comissão é de 25%.

for loop in range(10):
    nome = str(input("Nome do vendedor: "))
    preco = float(input("Valor do produto: "))
    vendas = int(input("Números de vendas: "))
    if (vendas >= 1 and vendas < 20):
        porc_comissao = 10
        valor_venda = preco * vendas
        comissao = (valor_venda * porc_comissao)/100
        valor_total = valor_venda + comissao
    elif (vendas >= 20 and vendas <= 49):
        porc_comissao = 15
        valor_venda = preco * vendas
        comissao = (valor_venda * porc_comissao)/100
        valor_total = valor_venda + comissao
    elif (vendas >= 50 and vendas <= 74):
        porc_comissao = 20
        valor_venda = preco * vendas
        comissao = (valor_venda * porc_comissao)/100
        valor_total = valor_venda + comissao
    elif (vendas >= 75):
        porc_comissao = 25
        valor_venda = preco * vendas
        comissao = (valor_venda * porc_comissao)/100
        valor_total = valor_venda + comissao
    else:
        porc_comissao = 0
        valor_venda = preco * vendas
        comissao = (valor_venda * porc_comissao)/100
        valor_total = valor_venda + comissao

    print("-------------------------------------")
    print(f"Nome do vendedor: {nome}\nPreço do produto: {preco:.2f}\nQuantidades de vendas: {vendas:.0f}\nValor total de vendas: {valor_venda:.2f}\nPorcentagem da comissão: {porc_comissao:.0f}\nValor da comissão: {comissao:.2f}\nValor vendas + comissão: {valor_total:.2f}")
    print("-------------------------------------")
