#Faça um algoritmo e o fluxograma que leia a idade de uma pessoa e informe a sua classe eleitoral:
#- não eleitor (abaixo de 16 anos)
#- eleitor obrigatório (entre 18 e 65 anos)
#- eleitor facultativo (entre 16 e 18 anos e maior de 65 anos)

idade = int(input("Informe a idade: "))

if (idade >= 18 and idade <= 65):
    print("Eleitor obrigatório")
elif (idade >= 16 and idade < 18 or idade > 65):
    print("Voto facultativo")
#elif (idade > 65):
#   print("Voto facultativo")
else:
    print("Não eleitor")