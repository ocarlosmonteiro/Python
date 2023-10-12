#Faça um algoritmo e o fluxograma que leia 40 números reais, somar e calcular a média dos números positivos e contar os números negativos e exiba os resultados.

repeticao = 0
positivo = 0
negativo = 0
soma = 0
media = 0

while (repeticao < 3):
    n = float(input("Digite um número: "))
    repeticao = repeticao + 1
    if (n >= 0):
        soma = soma + n
        media = soma / repeticao
    else:
        negativo = negativo + 1

print(f"A média dos 40 números é: {media:.2f}\nQuantidade de números negativos: {negativo:.0f}")