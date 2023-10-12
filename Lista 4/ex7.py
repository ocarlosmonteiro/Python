#Dada uma letra, escreva na tela se essa letra é ou não uma vogal. Utilize a função switch.

vogal = ["A","E","I","O","U","a","e","i","o","u"]

letra = str(input("Digite um letra: "))

match letra:
    case "A" | "a" | "E" | "e" | "I" | "i" | "O" | "o" | "U" | "u":
        print("Vogal")
    case _:
        print("Consoante")