dias = int(input ("Infforme a quantidades de dias: "))
horas = int(input("Informe as horas: "))
minutos = int(input("Informe os minutos: "))
segundos = int(input("Informe os segundos: "))

seg_r = (dias * 24 * 60 * 60) + (horas * 60 * 60) + (minutos * 60) + segundos

print("A quantidade de dias, horas, minutos e segundos informados são:",seg_r,"segundos")
