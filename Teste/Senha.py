senha = str(input("Digite a senha: "))
t = len (senha)

while (t < 8):
    senha = str(input("Digite a senha: "))
    t = len (senha)

conf_senha = str(input("Confirma a senha: "))

while (senha != conf_senha):

    conf_senha = str(input("Confirma a senha: "))
    print("Verificar senha e digitar novamente.")   
else:
    print("Cadastro realizado.")