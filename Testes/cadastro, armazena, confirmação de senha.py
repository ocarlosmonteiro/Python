arquivo = open("cadastro.txt", "w")


username = input("Cadastre um nome de usuário: ")
password = input("Cadastre uma senha: ")
password_c = input("Confirme a senha: ")
if password == password_c:
    print("Cadastro realizado com sucesso!")
else:
    print("Senhas estão diferentes")

arquivo.write(username + "\n")
arquivo.write(password)
arquivo.close()

