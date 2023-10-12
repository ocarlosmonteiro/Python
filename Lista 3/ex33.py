#Faça um algoritmo e o fluxograma que leia o nome, sexo e idade de uma pessoa. Se a pessoa for do sexo feminino e tiver menos que 25 anos então imprimir nome e a mensagem: ACEITA, caso contrário, imprimir nome e a mensagem: NÃO ACEITA. (Considerar f e F)

s = ["Masculino", "M", "m", "Feminino", "F", "f"]
f = ["Feminino", "F", "f"]

nome = str(input("Digite o nome: "))
sexo = str(input("Informe o sexo: "))
idade = int(input("Digite a idade: "))

if (sexo in f and idade < 25):
    print(f"{nome} ACEITA")
else:
    print(f"{nome} Não ACEITA(O)")