#Faça um algoritmo e o fluxograma que leia um número e imprimir uma das mensagens: maior do que 20, é igual a 20 ou é menor do que 20.

n = float(input("Digite um número: "))

if (n > 20):
    print(f"{n:.2f} é maior que 20")
elif (n < 20):
    print(f"{n:.2f} é menor que 20")
else:
    print(f"{n:.2f} é igual a 20")