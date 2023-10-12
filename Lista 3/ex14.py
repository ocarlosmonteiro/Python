#Faça um algoritmo e o fluxograma que leia o nome, a nota da PR1 e a nota da PR2 de 1 aluno. Imprimir: nome, nota da PR1, nota da PR2, média aritmética e uma das mensagens: AP, RP ou PF (a média é 7 para aprovação (AP), menor que 3 para reprovação (RP) e as demais em prova final (PF)).

nome = str(input("Digite o nome do aluno: "))
pr1 = float(input("Digite a nota da prova 1: "))
pr2 = float(input("Digite a nota da prova 2: "))
media = (pr1 + pr2)/2
if (media >= 7 and media <= 10):
    print(f"{nome}\nNota da prova 1: {pr1:.2f}\nNota da prova 2: {pr2:.2f}\nMédia: {media:.2f}\nAPROVADO.")
elif (media < 7 and media >= 3):
    print(f"{nome}\nNota da prova 1: {pr1:.2f}\nNota da prova 2: {pr2:.2f}\nMédia: {media:.2f}\nPROVA FINAL.")
elif (media < 3):
    print(f"{nome}\nNota da prova 1: {pr1:.2f}\nNota da prova 2: {pr2:.2f}\nMédia: {media:.2f}\nREPROVADO.")
else:
    print(f"{media:.2f} essa média é impossivel.")