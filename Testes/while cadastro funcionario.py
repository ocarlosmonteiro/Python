funcionarios = []
print("Digite 0 para terminar o cadastro")
while True:
    funcionario = input("Funcionário: ")
    funcionarios.append(funcionario)
    if funcionario == "0":
        print("encerrando")
        break
    print(funcionarios)
