#Escreva um programa com um procedimento que receba um inteiro entre 1 e 7, inclusive, e escreva o dia correspondente da semana (1 para domingo e 7 para sábado).

dia = int(input("Digite um número: "))

match dia:
    case 1:
        print("Domingo")
    case 2:
        print("Segunda")
    case 3:
        print("Terça")
    case 4:
        print("Quarta")
    case 5:
        print("Quinta")
    case 6:
        print("Sexta")
    case 7:
        print("Sábado")
    case _:
        print("Número inválido")