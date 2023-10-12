#Leia 4 variáveis A,B,C e D. A seguir, calcule e mostre a diferença do produto de A e B pelo produto de C e D (A*B-C*D).

a = float(input("Informe um número: "))
b = float(input("Informe outro número: "))
c = float(input("informe outro número: "))
d = float(input("Informe outro número: "))

prodAB = a * b
prodCD = c * d
dif = prodAB - prodCD

print(f"Produto entre A e B é: {prodAB}\nProduto entre C e D é: {prodCD}\nDiferença entre  os produtos é: {dif}")