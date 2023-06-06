# Leia o cateto oposto e o adjacente de um triangulo retangulo, calcule e mostre
# o cumprimento da hipotenusa
import math
ca = float(input('Digite o Comprimento do Cateto Adjacente '))
co = float(input('Digite o Comprimento do Cateto Adjacente '))

print('O Valor da Hipotenusa é de {:.2f}'.format(math.hypot(ca, co)))