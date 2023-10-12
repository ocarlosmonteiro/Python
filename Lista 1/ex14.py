#Leia 2 variáveis A e B, que correspondem a 2 notas de um aluno. A seguir, calcule a média do aluno, sabendo que a nota A tem peso 3 e a nota B tem peso 7.

a = float(input("informe a primeira nota: "))
b = float(input("Informe a segunda nota: "))

#media = ((a * 0.3) + (b * 0.7))
media = ((a * 3) + (b * 7))/10

print(f"Média foi : {media:.1f}")