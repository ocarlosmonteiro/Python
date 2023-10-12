#Faça um algoritmo e o fluxograma que leia o sexo (Masculino / Feminino) e o salário de 15 pessoas, calcule e exiba a média dos salários dos homens e das mulheres.

repeticao = 0
masc = 0
fem = 0
salario_m = 0
salario_f = 0
soma_salario_m = 0
soma_salario_f = 0
media_m = 0
media_f = 0

while (repeticao < 5):
    repeticao = repeticao + 1
    sexo = str(input("Informe o sexo (M - Masculino / F - Feminino): "))
    match sexo:
        case "M" | "m":
            masc = masc + 1
            salario_m = float(input("Informe salário: "))
            soma_salario_m = soma_salario_m + salario_m
            media_m = soma_salario_m / masc
        case "F" | "f":
            fem = fem + 1
            salario_f = float(input("Informe salário: "))
            soma_salario_f = soma_salario_f + salario_f
            media_f = soma_salario_f / fem
print(f"Média do salário masculino: {media_m:.2f}\nMédia salário feminino: {media_f:.2f}")