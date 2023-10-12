#Leia 3 variáveis A e B e C, que são as notas de um aluno. A seguir, calcule a média do aluno, sabendo que a nota A tem peso 2, a nota B tem peso 3 e a nota C tem peso 5.

a = float(input("Informe a primeira nota: "))
b = float(input("Informe a segunda nota: "))
c = float(input("informe a terceira nota: "))
media = (a * 0.2) + (b * 0.3) + (c * 0.5)

print(f"A média das notas é: {media:.1f}")