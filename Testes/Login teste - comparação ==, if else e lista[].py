user = ["carlos", "CARLOS", "Carlos", "cArlos", "caRlos", "CARlos"]
passw = "crm040199"

print("Login")
username = input("Informe seu usuário: ")
password = input("Informe sua senha: ")

if username in user and password == passw:
    print("Login efetuado com sucesso")
else:
    print("Usuário ou senha estão incorretos!")
 