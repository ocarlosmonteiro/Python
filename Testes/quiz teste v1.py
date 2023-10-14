print("\n*****************\nQUIZ\n*****************\n")
print("Realmente deseja jogar?\n 1- SIM\n 2- NÃO\n")
decisao_inicial = int(input("Informe a sua decisão: "))
if decisao_inicial == 1:
    print("Perfeito!!!\n\nIniciando o game...\n")
elif decisao_inicial == 2:
    print("És um peidão kkkkkkk\n\nDeseja realmente encerrar o jogo?\n 1-SIM\n 2-NÃO\n")
    decisao_inicial2 = int(input("Informe a sua decisão: "))
    if decisao_inicial2 == 1:
       print("És um peidão kkkkkkk\n")
       quit()
    elif decisao_inicial2 == 2:
        print("Perfeito!!!\n\nIniciando o game...")
else:
    print("\nInforme uma decisão válida!\n")
    while decisao_inicial != 1 or 2:
        decisao_inicial = int(input("Informe a sua decisão: "))
        break
