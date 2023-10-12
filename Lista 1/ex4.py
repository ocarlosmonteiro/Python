#O programa deverá ler os seguintes dados: número de horas que o funcionário trabalhou no mês, valor recebido por hora de trabalho.

valorHora = float(input("Informe valor hora que colaborador recebe: "))
horasTrabMes = float(input("Informe quantas hora foram trabalhadas no mês: "))

salarioBruto = valorHora * horasTrabMes

print(f"Salário bruto a receber é : {salarioBruto:.2f}")