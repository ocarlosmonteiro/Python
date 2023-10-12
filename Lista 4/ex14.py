#O conceito de um aluno é calculado a partir de sua nota, seguindo a tabela abaixo. Faça um programa que lê a nota de um aluno e imprimem seu conceito. O programa deve utilizar SWITCH. Assuma que alunos só podem receber notas inteiras (isto é, sem decimais).

#Nota     | 0 a 4 | 5 | 6 | 7 | 8 | 9+ | 
#Conceito |   F   | E | D | C | B |  A |

nota = int(input("Digite a nota: "))

match nota:
    case 0 | 1 | 2 | 3 | 4:
        print("Conceito F")
    case 5:
        print("Conceito E")
    case 6:
        print("Conceito D")
    case 7:
        print("Conceito C")
    case 8:
        print("Conceito B")
    case 9 | 10:
        print("Conceito A")
    case _:
        print("Nota inválida")
