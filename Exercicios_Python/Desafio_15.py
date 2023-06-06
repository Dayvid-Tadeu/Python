# Escreva um programa que pergunte a quantidade de KM percorridos por um carro alugado e a quantidade de dias
# de aluguel. Calcule o preço a pagar, sabendo que o carro custa R$ 60 por dia e R$ 0,15 por Km rodado
print('='*40)
km = float(input('Quantos Km seu carro percorreu? '))
alug = float(input('Quantos dias de você alugou o carro? '))

pkm = km * 0.15     # Preço por Km rodado, ou seja, 0,15 por Km
palug = alug * 60   # Preço do Aluguel, ou seja, 60 R$ por dia
total = pkm + palug # Soma de ambos
print('='*40)
print('Com {} Km percorridos e {} dias de aluguel, você pagará {:.2f} R$'.format(km, alug, total))
