
while True:
    n1 = int(input("Digite um número: "))
    n2 = int(input("Digite outro número: "))
    soma = n1 + n2
    print(n1,"+",n2,"=",soma)
    print("Deseja realizar outra soma? [S ou N]")
    continuar = input("Resposta: ")
    if continuar == "N":
        print("Encerrando")
        break
