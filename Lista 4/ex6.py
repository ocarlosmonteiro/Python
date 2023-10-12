#Faça um programa que: pergunte a mesada de um adolescente. Após isso pergunte se ele deseja comprar alguma coisa. O adolescente pode comprar produtos até o dinheiro acabar ou pode comprar somente o necessário.

mesada = float(input("Valor da mesada: "))

gastar = str(input("Deseja gastar o dinheiro, responda com 'Sim' ou 'Não': "))

match gastar:
    case "Sim" | "SIM" | "sim":
        
        valor_gastar = float(input("Valor a gastar: "))
        if (valor_gastar > mesada):
            print("Você ão tem dinheiro o suficiente")
        else:
            valor_atual = mesada - valor_gastar
            print(f"Você gastou: {valor_gastar:.2f}\nVocê tem disponivel: {valor_atual:.2f}")
                            
        
    case "Não" | "NÃO" | "não" | "Nao" | "NAO" | "nao":
        print(f"Ok\nVocê tem: {mesada:.2f}")