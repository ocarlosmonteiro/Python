for repeticao in range (3):
    nome = input("Informe um nome: ")
    n1 = float(input("Informe a primeira nota: "))
    while n1 > 10:
        print("Informe um número de 0 a 10!")
        n1 = float(input("Informe a primeira nota: "))
        break
    n2 = float(input("Informe a segunda nota: "))
    
    n3 = float(input("Informe a terceira nota: "))
    n4 = float(input("Informe a quarta nota: "))
    media = (n1+n2+n3+n4)/4
    print("A média de",nome,"é: ",media,)
 