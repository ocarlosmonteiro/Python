#O programa deverá ler o preço do produto em reais e o preço do dólar. 

dolar = 4.98

produto = float(input("Informe o favor do produto: "))

pDolar = produto * dolar

print(f"Valor do produto em dolar é: {pDolar:.2f}")


#:.2f - limita as casa decimais
#f - permite chamar variavel para ser exibida dentro de {}