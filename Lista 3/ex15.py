#Faça um algoritmo e o fluxograma que leia o nome da capital do Brasil. Se a resposta estiver correta, imprimir PARABÉNS, caso contrário, ERROU. (Considerar: BRASÍLIA ou Brasília).

resposta_correta = ["Brasília","BRASÍLIA","brasília","Brasilia","BRASILIA","brasilia"]

resposta = str(input("Qual a capital do Brasil?\n"))

if (resposta in resposta_correta):
    print("PARABÉNS!")
else:
    print("ERROUUUUU!")