#Faça um algoritmo e o fluxograma que leia 40 números reais, somar e calcular a média dos números positivos e contar os números negativos e exiba os resultados.

positivos = 0
negativos = 0
repeticao = 0
media = 0
soma = 0

for loop in range(3):
    n = float(input("Digite um número: "))
    repeticao = repeticao + 1
    if (n >= 0):
        soma = soma + n
        media = soma / repeticao
    else:
        negativos = negativos + 1

print(f"A médias dos 40 números é: {media:.1f}\nQuantidade de números negativos: {negativos:.0f}")