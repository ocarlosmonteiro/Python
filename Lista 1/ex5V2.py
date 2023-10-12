#O custo ao consumidor, de um carro novo, é a soma do custo de fábrica com a percentagem do distribuidor e dos impostos (aplicados ao custo de fábrica). Supondo que a percentagem do distribuidor seja de 28% e os impostos de 45%, definir as regras, escrever o algoritmo e o fluxograma para ler o custo de fábrica de um carro, calcular e escrever o custo ao consumidor.

custoFabrica = float(input("Valor de fabricação: "))

imposto = custoFabrica * 0.45
porcDistrib = custoFabrica * 0.28

custoConsum = imposto + porcDistrib + custoFabrica

print(f"Valor do veiculo para o cunsumidor será: {custoConsum:.2f}")