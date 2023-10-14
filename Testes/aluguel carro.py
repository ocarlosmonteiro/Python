kmPercorrido = float(input("Quantos KMs foram percorridos: "))
diasAlugados = int(input ("Quatos dias o carro ficou alugado: "))

pagar = (diasAlugados * 60) + (kmPercorrido * 0.15)
print("Valor a pagar é:",pagar)
