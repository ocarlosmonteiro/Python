AtributosTotal = int(10)
AtributosIncremento = int(5)

AtForca = 1
AtVeloc = 1
AtIntelig = 1
AtEmocional = 1
AtResist = 1

print(f"Força: {AtForca}\nVelocidade: {AtVeloc}\nInteligência: {AtIntelig}\nEmocional: {AtEmocional}\nResistência: {AtResist}")

aumentoAtributo = input("Qual atributo deseja aumentar:\n 1- Força\n 2- Velocidade\n 3- Inteligência\n 4- Emocional\n 5- Resistência\nEscolha:")

if aumentoAtributo == "1":
    AtForca = AtForca + 1
    AtributosIncremento = AtributosIncremento - 1
    print(f"Força: {AtForca}\nVelocidade: {AtVeloc}\nInteligência: {AtIntelig}\nEmocional: {AtEmocional}\nResistência: {AtResist}")
    print(f"Atributos disponiveis para upar: {AtributosIncremento}")

elif aumentoAtributo == "2":
    AtVeloc = AtVeloc + 1
    AtributosIncremento = AtributosIncremento - 1
    print(f"Força: {AtForca}\nVelocidade: {AtVeloc}\nInteligência: {AtIntelig}\nEmocional: {AtEmocional}\nResistência: {AtResist}")
    print(f"Atributos disponiveis para upar: {AtributosIncremento}")

elif aumentoAtributo == "3":
    AtIntelig = AtIntelig + 1
    AtributosIncremento = AtributosIncremento - 1
    print(f"Força: {AtForca}\nVelocidade: {AtVeloc}\nInteligência: {AtIntelig}\nEmocional: {AtEmocional}\nResistência: {AtResist}")
    print(f"Atributos disponiveis para upar: {AtributosIncremento}")

elif aumentoAtributo == "4":
    AtEmocional = AtEmocional + 1
    AtributosIncremento = AtributosIncremento - 1
    print(f"Força: {AtForca}\nVelocidade: {AtVeloc}\nInteligência: {AtIntelig}\nEmocional: {AtEmocional}\nResistência: {AtResist}")
    print(f"Atributos disponiveis para upar: {AtributosIncremento}")

elif aumentoAtributo == "5":
    AtResist = AtResist + 1
    AtributosIncremento = AtributosIncremento - 1
    print(f"Força: {AtForca}\nVelocidade: {AtVeloc}\nInteligência: {AtIntelig}\nEmocional: {AtEmocional}\nResistência: {AtResist}")
    print(f"Atributos disponiveis para upar: {AtributosIncremento}")
    