# Crie um programa que leia o nome completo da pessoa e mostre:
# O nome com todas as letras Maiúsculas
# O nome com todas as letras Minúsculas
# Quantas letras ao todo sem os espaços
# Quantas letras tem o primeiro nome

nome = input("Qual é o seu nome? ")
dividido = nome.split()
print('O Nome em Maiusculo fica {}'.format(nome.upper()))
print('O Nome em Minúsculo fica {}'.format(nome.lower()))
print('O Nome completo tem {} letras'.format(len(nome.replace(' ',''))))
print('O Primeiro nome é {} e tem {} letras'.format(dividido[0], len(dividido[0])))
#print(dividido[0])