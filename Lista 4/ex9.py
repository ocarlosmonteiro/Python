#Escreva um programa com uma função que receba um inteiro de 1 a 12 e retorne a quantidade de dias no mês correspondente (assume que o ano não é bissexto).

mes = int(input("Escolha um número entre 1 a 12: "))

while (mes < 1 or mes > 12):
    mes = int(input("Escolha um número entre 1 a 12: "))
    continue
        

match mes:
    case 1:
        print("Janeiro - 31 dias")
    case 2:
        print("Fevereiro - 28 dias")
    case 3:
        print("Março - 31 dias")
    case 4:
        print("Abril - 30 dias")
    case 5:
        print("Maio - 31 dias")
    case 6:
        print("Junho 30 dias")
    case 7:
        print("Julho - 31 dias")
    case 8:
        print("Agosto - 31 dias")
    case 9:
        print("Setembro - 30 dias")
    case 10:
        print("Outubro - 31 dias")
    case 11:
        print("Novembro - 30 dias")
    case 12:
        print("Dezembro - 31 dias")
