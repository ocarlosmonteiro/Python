#Faça um algoritmo e o fluxograma que leia 50 números inteiros, conte quantos são divisíveis por 3 e exiba o resultado.

divisivel = 0
nao_divisivel = 0

for loop in range(50):
    n = int(input("Digite um núemro: "))
    divisao = n % 3
    if (divisao == 0):
       divisivel = divisivel + 1
    else:
       nao_divisivel = nao_divisivel + 1

print(f"Número divisel por 3: {divisivel:.0f}\nNúmero não divisivel por 3: {nao_divisivel:.0f}")
