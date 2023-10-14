AtributosTotal = 10
AtributosIncremento = 5

AtForca = 1
AtVeloc = 1
AtIntelig = 1
AtEmocional = 1
AtResist = 1

print(f"Força: {AtForca}\nVelocidade: {AtVeloc}\nInteligência: {AtIntelig}\nEmocional: {AtEmocional}\nResistência: {AtResist}")

while AtributosIncremento > 0:
    aumentoAtributo = input("Qual atributo deseja aumentar:\n 1- Força\n 2- Velocidade\n 3- Inteligência\n 4- Emocional\n 5- Resistência\nEscolha:")

    if aumentoAtributo == "1":
        AtForca += 1
        AtributosIncremento -= 1
    elif aumentoAtributo == "2":
        AtVeloc += 1
        AtributosIncremento -= 1
    elif aumentoAtributo == "3":
        AtIntelig += 1
        AtributosIncremento -= 1
    elif aumentoAtributo == "4":
        AtEmocional += 1
        AtributosIncremento -= 1
    elif aumentoAtributo == "5":
        AtResist += 1
        AtributosIncremento -= 1

    print(f"Força: {AtForca}\nVelocidade: {AtVeloc}\nInteligência: {AtIntelig}\nEmocional: {AtEmocional}\nResistência: {AtResist}")
    print(f"Atributos disponíveis para upar: {AtributosIncremento}")
