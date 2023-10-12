#João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário de seu trabalho. Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do estado de São Paulo (50 quilos) deve pagar um multa de R$ 4,00 por quilo excedente. João precisa que você faça um diagrama de blocos que leia a variável P (peso de peixes) e verifique se há excesso. Se houver, gravar na variável E (Excesso) e na variável M o valor da multa que João deverá pagar. Caso contrário mostrar tais variáveis com o conteúdo ZERO.

p = float(input("Informe o peso da pesca: "))

if (p > 50):
    m = (p - 50) * 4.00
    print(f"Peso: {p:.2f}\nMulta a pagar: {m:.2f}")
else:
    print(f"Peso: {p:.2f}\nNão há multa a ser paga.")