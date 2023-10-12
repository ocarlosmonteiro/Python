#Faça um algoritmo e o fluxograma em Pascal que leia um numero N, some todos os números inteiros entre 1 e N, e mostre o resultado obtido. 

repetir = 0
n = 0
somaN = 0

n = int(input("Digite valor de N: "))

while (repetir < n):
    repetir = repetir + 1
    n = int(input("Digite valor de N: "))
    somaN = somaN + n

print(f"Valor da soma de Ns é: {somaN:0f}")