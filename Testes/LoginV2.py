arquivo = open("CadastroLoginV2.txt", "r")

CadastroLoginV2 = arquivo.readlines()

arquivo.close()

CadastroLoginV2 = [nome_usuario.strip() for nome_usuario in CadastroLoginV2]

l_nome_usuario = input("Digite o nome de usuário: ")

encontrado = False
for nome_usuario in CadastroLoginV2:
    if l_nome_usuario == nome_usuario:
        encontrado = True
        break
if encontrado:
    print(l_nome_usuario, "foi encontrado no arquivo.")
else:
    print(l_nome_usuario, "não foi encontrado no arquivo.")
