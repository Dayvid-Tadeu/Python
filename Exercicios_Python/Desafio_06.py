# Crie um algoritmo que leia um numero e mostre o seu Dobro, Triplo e Raiz Quadrada
num = int(input('Digite um número: '))

print('='*30)
print('O Dobro de {} é {}'.format(num, num * 2))
print('O Triplo de {} é {}'.format(num, num * 3))
print('A Raiz de {} é {:.2f}'.format(num, num ** (1/2)))