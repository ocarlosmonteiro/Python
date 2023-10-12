#Implemente uma função chamada menu que imprima o seguinte menu na tela e em seguida leia e que retorne o número da opção escolhida.
#1. Soma
#2. Média
#3. Menor
#4. Maior

menu = int(input("Selecione a operação:\n1 - Soma\n2 -Média\n3 - Menor\n4- Maior\n\nOpção: "))

match menu:
    case 1:
        print("1 - Soma")
    case 2:
        print("2 - Média")
    case 3:
        print("3 - Menor")
    case 4:
        print("4 - Maior")
    case _:
        print("Opção inválida")