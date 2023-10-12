#Faça um algoritmo e o fluxograma que leia um número e informe se ele é divisível por 3 e por 5.

n = int(input("Digite um número: "))

d3 = n % 3
d5 = n % 5

if (d3 == 0 and d5 == 0):
    print(f"{n:.0f} é divisivel por 3 e por 5.")
elif (d3 == 0 and d5 != 0):
    print(f"{n:.0f} é divisivel por 3, porém não por 5.")
elif (d3 != 0 and d5 == 0):
    print(f"{n:.0f} não é divisivel por 3, porém é por 5.")
else:
    print(f"{n:.0f} não é divisivel por 3 e nem por 5.")