#Crie um programa que funcione como um “encantômetro” ou seja, um painel eletrônico onde o cliente de uma determinada loja deixa sua opinião, pressionando um botão para variar entre as opções ÓTIMO, BOM, REGULAR e RUIM, e outro para confirmar o voto.

opiniao = int(input("1 - ÓITMO\n2 - BOM\n3 - REGULAR\n4 - RUIM\n\nQual a sua opinião sobre a loja: "))

match opiniao:
    case 1:
        print("ÓTIMO!")
    case 2:
        print("BOM!")
    case 3:
        print("REGULAR!")
    case 4:
        print("RUIM!")

confima = str(input("Confirmar opinião\nS - SIM\nN - NÃO\n"))

match confima:
    case "S" | "s":
        print("CONFIRMADO!!!")
    case "N" | "n":
        print("NÃO CONFIRMADO")