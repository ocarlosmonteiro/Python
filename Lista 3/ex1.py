#Faça um algoritmo e o fluxograma que leia um número e imprima caso seja maior do que 20.

n = float(input("Informe um número: "))

if n >= 20:
    print(f"número digitado é: {n:.1f}")
else:
    print("Número menor que 20!")