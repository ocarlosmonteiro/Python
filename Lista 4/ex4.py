#Faça um programa que leia um número entre 0 e 10, e escreva este número por extenso. Use o comando switch.

n = int(input("Digite um número de 0 a 10: "))

while (n < 0 or n > 10):
    n = int(input("Tu é burro, o caralho!\nDigite um número de 0 a 10: "))

match n:
    case 0:
        print("ZERO")
    case 1:
        print("UM")
    case 2:
        print("DOIS")
    case 3:
        print("TRÊS")
    case 4:
        print("QUATRO")
    case 5:
        print("CINCO")
    case 6:
        print("SEIS")
    case 7:
        print("SETE")
    case 8:
        print("OITO")
    case 9:
        print("NOVE")
    case 10:
        print("DEZ")