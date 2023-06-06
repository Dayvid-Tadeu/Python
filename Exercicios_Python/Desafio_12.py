# Faça um programa que leia o preço de um produto e mostre seu novo preço com 5% de desconto.
print('='*30)
p1 = float(input('Qual o preço do Produto? '))
print('='*30)

p2 = p1 - (p1 * (5*(1/100)))

print('O Produto de {}R$ com 5%''de desconto será de {:.2f}R$'.format(p1, p2))