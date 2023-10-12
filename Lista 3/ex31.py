#Faça um algoritmo e o fluxograma que leia o ano de nascimento de uma pessoa e o ano atual. Imprima a idade da pessoa. Não se esqueça de verificar se o ano de nascimento é um ano válido, isto é, é menor que o ano atual.

anoAtual = int(input("Digite o ano atual: "))
dataNasc = int(input("Digite o ano de nascimento: "))

idade = anoAtual - dataNasc

if (dataNasc <= anoAtual):
    print(f"Idade é: {idade:.0f}")
else:
    print("Ano de nascimento tem que ser menor que o ano atual")