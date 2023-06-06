# Faça um programa que leia um inteiro e mostre o seu sucessor e antecessor
num = int(input('Digite um Número '))
ant = num - 1
suc = num + 1
print('='*20)
print('O Antecessor de {} é {}'.format(num, ant))
print('O Sucessor de {} é {}'.format(num, suc))
