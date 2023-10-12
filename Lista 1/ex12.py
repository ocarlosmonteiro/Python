#Elabore um programa que leia a quantidade de chuva em polegadas e imprima a equivalente em milímetros (25,4 mm = 1 polegada).

polegadas = float(input("Informe quanto choveu em polegadas: "))

milimetros = 25.4 * polegadas

print(f"Choveu {polegadas:.1f} polegadas que é igual a {milimetros:.1f} milimetros.")