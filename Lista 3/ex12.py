#Faça um algoritmo e o fluxograma que leia um número e indique se o número digitado está compreendido entre 20 e 90 ou não

n = int(input("Digite um número: "))

if (n >= 20 and n <= 90):
    print(f"{n:.0f} está entre 20 e 90.")
else:
    print(f"{n:.0f} não está entre 20 e 90")