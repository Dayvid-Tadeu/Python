# Quanto de dinheiro uma pessoa tem e mostre o quanto ela pode comprar em Dollar.
reais = float(input('Quanto dinheiro você tem? '))
dollar = float(input('Qual a cotação do Dollar hoje? '))

conv = reais / dollar

print('Com {:.2f} Reais você poderia comprar {:.2f} Dolares na cotação de hoje.'.format(reais, conv))