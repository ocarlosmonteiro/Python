#O custo ao consumidor de um carro novo é a soma do custo de fábrica com a percentagem do distribuidor e dos impostos (aplicados ao custo de fábrica). Supondo que a percentagem do distribuidor seja de 12% e os impostos 45%, preparar um programa para ler o custo de fábrica do carro e imprimir o custo ao consumidor.

custoFab = float(input("Informe o custo de fabricação: "))
porcDist = custoFab * 0.12
imposto = custoFab * 0.45

custoCons = custoFab + porcDist + imposto

print(f"Custo de distribuição é: {custoCons:.2f}")