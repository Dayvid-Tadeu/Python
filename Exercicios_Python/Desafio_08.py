# Leia um numero em Metros e converta em Centimetros e Milimetros.
# 1 Metro é 100 cm
# 1 Metro é 1000 mm

num = float(input('Digite um número em metros '))
print('{} metros é equivalente a {} cm'.format(num, num * 100))
print('{} metros é equivalente a {} mm'.format(num, num * 1000))