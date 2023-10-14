cadastro = []
 
nome = str(input("Digite seu nome: "))
username = str(input("Digite seu nome de usuário: "))
senha = str(input("Digite a senha: "))

cadastro.append(nome + username + senha)

print("Nome: {}\nNome de usuário: {}\nSenha: {}".format(nome, username,senha))