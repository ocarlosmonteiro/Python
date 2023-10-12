#Desenvolva um programa de uma eleição com os seguintes candidatos e com os seguintes códigos de eleição:
#0 – Votos Brancos
#1 – Patolino
#2 - Frajola
#3 – Pernalonga
#4 – Gaguinho
#5 – Papa-Léguas
#6 – Taz
#Exiba para o usuário qual candidato ele votou. Se o usuário digitar qualquer outro número que não seja o da lista informe para ele que o mesmo anulou o seu voto.

voto = int(input("0 – Votos Brancos\n1 – Patolino\n2 - Frajola\n3 – Pernalonga\n4 – Gaguinho\n5 – Papa-Léguas\n6 – Taz\n\nInsira o código do canditato: "))

match voto:
    case 0:
        print("Voto em branco")
    case 1:
        print("Seu voto foi para o Patolino")
    case 2:
        print("Seu voto foi para o Frajola")
    case 3:
        print("Seu voto foi para o Pernalonga")
    case 4:
        print("Seu voto foi para o Gaguinho")
    case 5:
        print("Seu voto foi para o Papa Léguas")
    case 6:
        print("Seu voto foi para o Taz")
    case _:
        print("Você anulou seu voto")