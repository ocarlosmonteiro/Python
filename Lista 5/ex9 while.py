#Em  uma  pesquisa  perguntou-se  a  cada  aluno  quantas  refeições  fez  no  mês anterior.  Faça  um  algoritmo  e  o  fluxograma  que  leia  o  número  de  refeições diárias de 350 alunos e calcule e exiba: 
#- o número de alunos que fez menos de 10 refeições no mês; 
#- o número de alunos que fez entre 10 e 20 refeições; e 
#- o número de alunos que fez mais de 20 refeições.

repeticao = 0
menos10 = 0
entre10a20 = 0
mais20 = 0
naocomeram = 0

while (repeticao < 350):
    refeicao = int(input("Quantidade de refeições no mês anterior: "))
    repeticao = repeticao + 1
    if (refeicao >= 1 and refeicao < 10):
        menos10 = menos10 + 1
    elif (refeicao >= 10 and refeicao <= 20):
        entre10a20 = entre10a20 + 1
    elif (refeicao > 20):
        mais20 = mais20 + 1
    else:
        naocomeram = naocomeram + 1
print(f"Quantidade de refeição realizada pelos alunos no mês anterior:\nMenos que 10: {menos10:.0f}\nEntre 10 e 20: {entre10a20:.0f}\nMais que 20: {mais20:.0f}\nNão comeram: {naocomeram:.0f}")