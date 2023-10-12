#Faça um algoritmo e o fluxograma que leia o nome e a idade de 20 pessoas, calcule e exiba a média das idades.

repeticao = 0
soma = 0
media = 0

while (repeticao < 20):
    idade = int(input("Digite a idade: "))
    repeticao = repeticao + 1
    soma = soma + idade
    media = soma / repeticao

print(f"A média das 20 idades é: {media:.1f}")