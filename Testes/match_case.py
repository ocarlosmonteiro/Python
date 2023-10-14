escolha = input("Escolha um número: ")

match escolha:
    case "1":
        print("Um")
    case "2":
        print("Dois")
    case "3":
        print("Três")
    case _:
        print("Outro número")
