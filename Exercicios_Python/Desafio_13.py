# Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário com 15% de aumento.
print('='* 40)
sal1 = (float(input('Qual é o seu Salário? ')))
print('='* 40)

sal2 = sal1 + (sal1 * (15*(1/100)))

print('Seu Salário de {}R$ com 15%'' de aumento será de {:.2f}R$'.format(sal1, sal2))