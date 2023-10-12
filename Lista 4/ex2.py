#Suponha que você atrasou uma conta. A cada mês que você deixa de pagar, será cobrado 1% de juros no valor inicial. Ou seja, se você atrasar um mês, irá pagar 1%. Se atrasar 3 meses, irá pagar 3% etc. Vamos supor que você pode atrasar, no máximo, 5 meses.
#O programa pede, como entrada, dois valores:
# - Um float: com o valor de sua dívida inicial (valor_i)
# - Um inteiro: de 0 até 5, que são os meses de atraso.

valor_i = float(input("Valor da conta: "))
atraso = int(input("Meses em atraso: "))

while (atraso < 1 or atraso > 5):
    print("Quantidade de meses invalida!")
    atraso = int(input("Meses em atraso: "))

match atraso:
    case 1:
        valor_a = valor_i + (valor_i * 0.01)
    case 2:
        valor_a = valor_i + (valor_i * 0.02)
    case 3:
        valor_a = valor_i + (valor_i * 0.03)
    case 4:
        valor_a = valor_i + (valor_i * 0.04)
    case 5:
        valor_a = valor_i + (valor_i * 0.05)

print(f"Valor da conta: {valor_i:.2f}\nValor com atraso de {atraso:.0f}: {valor_a:.2f}")