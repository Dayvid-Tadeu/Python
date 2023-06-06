# Crie um programa que leia um Real qualquer e mostre sua porção inteira
# Exemplo: 6.123 = 6
import math

x = float(input('Digite um Número Real '))
print('O Numero inteiro de {} é {}'.format(x, math.trunc(x)))