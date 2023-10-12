#Faça um algoritmo e o fluxograma que leia um número e informar se ele é divisível por 10, ou é divisível por 5, ou é divisível por 2 ou se não é divisível por nenhum destes

n = int(input("Digite um número: "))

d10 = n % 10
d5 = n % 5
d2 = n % 2

if (d10 == 0):
    print(f"{n:.0f} é divisivel por 10")
elif (d5 == 0):
    print(f"{n:.0f} é divisivel por 5")
elif (d2 == 0):
    print(f"{n:.0f} é divisivel por 2.")
else:
    print(f"{n:.0f} não é divisivel por 10, 5 e nem por 2")