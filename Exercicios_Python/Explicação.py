print('Olá Mundo!!!') # O Print escreve na tela

print(7 + 4) # Escreve 11 na tela

print('7'+'4') # Junta formando 74

nome = "Dayvid"
idade = 38
peso = 85.2
print(nome, idade, peso)

nome = input("Qual é o Seu Nome ? ")
idade = input("Qual é a sua Idade ? ")
peso = input("Qual é o seu Peso ? ")
print('Seu nome é',nome,'e você tem', idade,'anos de idade e seu peso é', peso,'Kg')

#--------------TIPOS PRIMITIVOS-------------------------------
# int -  inteiro
# float - reais
# bool - true or false
# str - caracteres

#----------------OPERAÇÕES ARITIMÉTICAS------------------
# + adiçãp
# - Subtração
# * Multiplicação
# / divisão
# ** potencia
# // divisão inteira
# % modulo ou resto da divisão

# OBD Igual é (==)
# Para potencia tbm usamos pow(a, b) a elevado a b
# Podemos usar Raiz Quadrada de 81 como 81**(1/2)
# Podemos fazer print('='*20) ou '='*20 repete = 20 vezes

# Ordem -> {()},  {**},  {*/ // %},  {+ -}  

a = int(input('Digite um numero: '))
b = int(input('Digite outro numero: '))
soma = (a + b)
sub = (a - b)
mul = (a * b)
div = (a / b)
pot = (a ** b)
divin = (a // b)
mod = (a % b)

print('SOMA {}'.format(soma))
print('SUBTRAÇÃO {}'.format(sub))
print('MULTIPLICAÇÂO {}'.format(mul))
print('DIVISÃO {}'.format(div))
print('POTENCIA {}'.format(pot))
print('DIVISÃO INTEIRA {}'.format(divin))
print('MÓDULO {}'.format(mod))

# ----------------------------------

nome = input('Qual é o seu Nome? ')
print('Prazer em conhecer você, {:20}!!!'.format(nome)) # Dá espaço de 20 Caracteres
print('Prazer em conhecer você, {:<20}!!!'.format(nome)) # Dá espaço a esquerda
print('Prazer em conhecer você, {:>20}!!!'.format(nome)) # Dá espaço a direita
print('Prazer em conhecer você, {:^20}!!!'.format(nome)) # Centraliza
print('Prazer em conhecer você, {:=^20}!!!'.format(nome)) # Preenche os espaços com (=)

# -------------------CAP 08 ------------------
# Import doce (Importa todos os doces)
# From doce import bolo (Importa só bolo de todos os doces)
# Import math
# From math import sqrt
# math.ceil() - arredonda para cima
# math.floor() - arredonda para baixo

import math
num = int(input('Digite um numero '))
raiz = math.sqrt(num)

print('A raiz de {} é igual a {}'.format(num, math.ceil(raiz)))

# Outra forma de import------------------

from math import sqrt
num = int(input('Digite um numero '))
raiz = sqrt(num)

print('A raiz de {} é igual a {}'.format(num, raiz))

# Com duas funções de uma biblioteca-----------------

from math import sqrt, floor
num = int(input('Digite um numero '))
raiz = sqrt(num)

print('A raiz de {} é igual a {}'.format(num, floor(raiz))

# Escolha de numero ente 0 e 1
import random
num = random.random()
print(num)

# Escolha de numero ente 0 e 10
import random
num = random.randint(1, 10)
print(num)

# Lição apartir do desafio 21, pois os outros foram corrigidos