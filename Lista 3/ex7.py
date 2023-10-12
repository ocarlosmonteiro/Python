#Elabore um algoritmo e o fluxograma que dada a idade de um nadador classifique-o em uma das seguintes categorias:
# - Infantil A = 5 a 7 anos
# - Infantil B = 8 a 11 anos
# - Juvenil A = 12 a 13 anos
# - Juvenil B = 14 a 17 anos
# - Adultos = Maiores de 18 anos

idade = int(input("Idade do nadador: "))

if (idade >= 5 and idade <= 7):
    print(f"Idade: {idade:.0f}\nCategoria INFANTIL A!")
elif (idade >= 8 and idade <= 11):
    print(f"Idade: {idade:.0f}\nCategoria INFANTIL B!")
elif (idade >= 12 and idade <= 13):
    print(f"Idade: {idade:.0f}\nCategoria JUVENIL A!")
elif (idade >=14 and idade <= 17):
    print(f"Idade: {idade:.0f}\nCategoria JUVENIL B!")
elif (idade >= 18):
    print(f"Idade: {idade:.0f}\nCategoria ADULTOS!")
else:
    print(f"Não há categorias para menores de 5 anos!")