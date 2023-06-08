# Faça um programa que leia um numero de 0 a 9999 e mostre os digitos separados em:
# unidade, dezena, centena e milhar
num = int(input('Digite um numero entre 0 a 9999: '))

# Calcula a Unidade
unid = num % 10

#Calcula a Dezena
numdez = (num - unid)/10
dez = numdez % 10

#Calcula a Centena
numcent = (numdez - dez)/10
cent = numcent % 10
#Calcula a Milhar
nummil = (numcent - cent)/10
mil = nummil % 10

print('O Número digitado foi {}'.format(num))
print('A MILHAR é {:.0f}'.format(mil))
print('A CENTENA é {:.0f}'.format(cent))
print('A DEZENA é {:.0f}'.format(dez))
print('A UNIDADE é {:.0f}'.format(unid))


# Ou Podemos executar com o Código abaixo

# x = int(input('Digite um numero: '))
# num = str(x)
# print('Milhar: {}'.format(num[3]))
# print('Centena: {}'.format(num[2]))
# print('Dezena: {}'.format(num[1]))
# print('Unidade: {}'.format(num[0]))
