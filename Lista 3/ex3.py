#Elabore um algoritmo e o fluxograma que leia as variáveis C e N, respectivamente código e número de horas trabalhadas de um operário. E calcule o salário sabendo-se que ele ganha R$ 10,00 por hora. Quando o número de horas exceder a 50 calcule o excesso de pagamento armazenando-o na variável E, caso contrário zerar tal variável. A hora excedente de trabalho vale R$ 20,00. No final do processamento imprimir o salário total e o salário excedente.

c = int(input("informe código do colaborador: "))
n = int(input("Informe número de horas trabalhadas: "))


if (n > 50):
    e = (n - 50)
    salarioE = e * 20.00
    salario = n * 10
    salarioTotal = salario + salarioE
    print(f"Código do colaborador:{c}\nSalário excedente: {salarioE:.2f}\nSalário total: {salarioTotal:.2f}")
else:
    salarioTotal = n * 10.00
    print(f"Código do colaborador: {c}\nSalário total é: {salarioTotal:.2f}\nNão há salário excedente.")