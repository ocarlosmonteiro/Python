#A Secretaria de Meio Ambiente que controla o índice de poluição mantém 3 grupos de indústrias que são altamente poluentes do meio ambiente. O índice de poluição aceitável varia de 0,05 até 0,25. Se o índice sobe para 0,3 as indústrias do 1º grupo são intimadas a suspenderem suas atividades, se o índice crescer para 0,4 as industrias do 1º e 2º grupo são intimadas a suspenderem suas atividades, se o índice atingir 0,5 todos os grupos devem ser notificados a paralisarem suas atividades. Faça um algoritmo e o fluxograma que leia o índice de poluição medido e emita a notificação adequada aos diferentes grupos de empresas.

indiceP = float(input("Informe indice de poluição: "))

if (indiceP >= 0.05 and indiceP <= 0.25):
    print(f"Indice de poluição {indiceP:.2f}, está aceitavel")
elif (indiceP >= 0.26 and indiceP <0.3):
    print(f"Indice de poluição: {indiceP:.2f}, atenção, pode haver suspensão das atividades do grupo 1!")
elif (indiceP >= 0.3 and indiceP < 0.4):
    print(f"Indice de poluição: {indiceP:.2f}, suspender atividades das industrias do grupo 1")
elif (indiceP >= 0.4 and indiceP < 0.5):
    print(f"Indice de poluição: {indiceP:.2f}, suspender atividades das industrias dos grupos 1 e 2")
elif(indiceP >= 0.5):
    print(f"Indice de poluição: {indiceP:.2f}, suspender atividades das industrias dos grupos 1, 2 e 3")
else:
    print("Indice de poluição está baixo")