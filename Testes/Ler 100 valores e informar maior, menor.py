valores = []
for loop in range(100):
    valor = int(input("Informe um valor: "))
    valores.append(valor)

print(valores)
print(f"Maior valor é: {max(valores)}")
print(f"Menor valor é: {min(valores)}")
