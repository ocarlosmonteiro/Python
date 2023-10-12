#Um funcionário irá receber um aumento de acordo com o seu plano de trabalho, de acordo com a tabela abaixo:
# Plano | Aumento
#   A       10%     
#   B       15%
#   C       20%
#Faça um programa que leia o plano de trabalho e o salário atual de um funcionário e calcula e imprime o seu novo salário. Use o comando switch.

plano = ["A","B","C","a","b","c"]

plano_t = str(input("Digite o plano de trabalho: "))
salario_atual = float(input("Salário atual: "))

while (plano_t not in plano):
    print("Plano invalido")
    plano_t = str(input("Digite o plano de trabalho: "))

match plano_t:
    case "A" | "a":
        salario_ajuste = salario_atual + (salario_atual * 0.10)
    case "B" | "b":
        salario_ajuste = salario_atual + (salario_atual * 0.15)
    case "C" | "c":
        salario_ajuste = salario_atual + (salario_atual * 0.20)
print(f"Salário atual: {salario_atual:.2f}\nPlano: {plano_t}\nSalário ajustado: {salario_ajuste:.2f}")