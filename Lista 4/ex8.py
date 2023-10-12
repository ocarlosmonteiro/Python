#Faça um programa que informe o mês de acordo com o número informado pelo usuário. (Exemplo: Entrada: 4. Saída: Abril).

mes = int(input("Escolha um número entre 1 a 12: "))

while (mes < 1 or mes > 12):
    mes = int(input("Escolha um número entre 1 a 12: "))
    continue
        

match mes:
    case 1:
        print("Janeiro")
    case 2:
        print("Fevereiro")
    case 3:
        print("Março")
    case 4:
        print("Abril")
    case 5:
        print("Maio")
    case 6:
        print("Junho")
    case 7:
        print("Julho")
    case 8:
        print("Agosto")
    case 9:
        print("Setembro")
    case 10:
        print("Outubro")
    case 11:
        print("Novembro")
    case 12:
        print("Dezembro")
