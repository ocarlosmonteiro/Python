#Um total de 500 alunos de uma universidade foram entrevistados. De cada um deles foram colhidas as seguintes informações: o código do curso que freqüenta (1-engenharia; 2-computação; 3-administração) e a idade. Faça um algoritmo e o fluxograma que processe estes dados e que forneça as seguintes informações: 
#- número de alunos por curso; 
#- número de alunos com idade entre 20 e 25 anos, por curso; e 
#- qual o curso com menor média de idade. 

engenharia = 0
computacao = 0
administracao = 0
qtdIdadeEng = 0
qtdIdadeComp = 0
qtdIdadeAdm = 0
somaIdadeEng = 0
mediaIdadeEng = 0
somaIdadeComp = 0
mediaIdadeComp = 0
somaIdadeAdm = 0
mediaIdadeAdm = 0



for loop in range(500):
    codCurso = int(input("Código do curso: "))
    idade = int(input("Sua idade: "))

    match codCurso:
        case 1:
            engenharia = engenharia + 1
            if (idade >= 20 and idade <= 25):
                qtdIdadeEng = qtdIdadeEng + 1
            somaIdadeEng = somaIdadeEng + idade
            mediaIdadeEng = somaIdadeEng / engenharia
        case 2:
            computacao = computacao + 1
            if (idade >= 20 and idade <= 25):
                qtdIdadeComp = qtdIdadeComp + 1
            somaIdadeComp = somaIdadeComp + idade
            mediaIdadeComp = somaIdadeComp / computacao
        case 3:
            administracao = administracao + 1
            if (idade >= 20 and idade <= 25):
                qtdIdadeAdm = qtdIdadeAdm + 1
            somaIdadeAdm = somaIdadeAdm + idade
            mediaIdadeAdm = somaIdadeAdm / administracao

if (mediaIdadeEng < mediaIdadeComp and mediaIdadeEng < mediaIdadeAdm):
    menorMediaIdade = "Engenharia"
elif (mediaIdadeComp < mediaIdadeAdm and mediaIdadeComp < mediaIdadeEng):
    menorMediaIdade = "Computação"
elif (mediaIdadeAdm < mediaIdadeComp and mediaIdadeAdm < mediaIdadeEng):
    menorMediaIdade = "Administração"
print(f"Engenharia:\n Quantidade de alunos: {engenharia:.0f}\n Alunos entre 20 e 25 anos: {qtdIdadeEng:.0f}")
print(f"Computação:\n Quantidade de alunos: {computacao:.0f}\n Alunos entre 20 e 25 anos: {qtdIdadeComp:.0f}")
print(f"Administração:\n Quantidade de alunos: {administracao:.0f}\n Alunos entre 20 e 25 anos: {qtdIdadeAdm:.0f}")
print(f"Curso com a menor média de idade: {menorMediaIdade}")