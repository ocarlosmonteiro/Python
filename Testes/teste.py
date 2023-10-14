# Abre o arquivo em modo de escrita
arquivo = open("nomes.txt", "w")

# Cria uma variável para controlar a inserção de nomes
continuar = True

# Loop para inserir nomes no arquivo
while continuar:
    # Solicita ao usuário um nome para ser adicionado
    nome = input("Digite um nome para adicionar ao arquivo (ou 'sair' para finalizar): ")

    # Verifica se o usuário deseja sair do loop
    if nome == "sair":
        continuar = False
    else:
        # Escreve o nome no arquivo
        arquivo.write(nome + "\n")

# Fecha o arquivo
arquivo.close()

print("Nomes armazenados com sucesso no arquivo!")
