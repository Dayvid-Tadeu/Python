#Faça um programa que leia a largura e altura de uma parede em metros e calcule a sua área
# e a quantidade de tinta necessária para pintá-la, sabendo que cada litro pode pintar 2 metros quadrados.
print('='*30)
lar = float(input('Qual a Largura? '))
alt = float(input('Qual a Altura? '))

area = lar * alt
tinta = area/2

print('='*30)
print('A dimensão da sua parede é {} x {},'.format(alt, lar))
print('Desta forma usaremos {} litros de tinta'.format(tinta))