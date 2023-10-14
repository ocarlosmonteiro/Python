arquivo = open("CadastroLoginV2.txt", "w")

nome_completo = input("Digite seu nome completo: ")
nome_usuario = input("Digite seu nome de usuário: ")
senha = input("Digite a senha: ")
confirme_senha = input("Confirme a senha: ")

if senha == confirme_senha:
    print("TUDO CORRETO\nCADASTRO REALIZADO")
    
else:
    print("Senha incorreta")
    while senha != confirme_senha:
        print("Por favor, confirme a senha corretamente.")
        confirme_senha = input("Confirme a senha: ")
        if senha == confirme_senha:
            print("TUDO CORRETO\nCADASTRO REALIZADO")
            break
arquivo.write(nome_completo + "\n" + nome_usuario + "\n" + senha)
arquivo.close()
