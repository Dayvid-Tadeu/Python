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

# MANIPULANDO TEXTOS - AULZ 09
frase = 'Curso em Video Python'
print(frase[9])      # Aparece a letra 'V'
print(frase[9:13])   # Aparece 'Vide' pois a letra 'O' ele tira
print(frase[9:21:2]) # Aparece 'VdoPto' pois pula de 2 em 2
print(frase[:5])     # Aparece 'Curso' pois vai do primeiro até o caractere 5
print(frase[15:])    # Aparece 'Python'
print(frase[9::3])   # Aparece 'VePh' vai do V até o final pulando de 3 em 3.

#len vem de lenght 'tamanho"
print(len(frase))             # Mostra o tamanho da frase
print(frase.count('o'))       # Mostra a quantas vezes aparece a letra 'O'
print(frase.count('o',0, 13)) # Mostra a quantas vezes aparece a letra 'O' no intervelo dos 13 primeiros caracateres
print(frase.find('deo'))      # Mostra onde começa 'deo' dentro da cadeia de caracteres
print(frase.replace('Python', 'Android')) # Ele troca a palavra 'Python' por 'Android' dentro ada cadeia de caracateres
print(frase.upper())          # Mostra a frase toda com letras maiusculas
print(frase.lower())          # Mostra a frase toda com letras minusculas
print(frase.strip())          # Retira os espaços não usados no começo e no fim de uma cedeia de caracteres
print(frase.rstrip())         # Retira os espaços não usados na direita
print(frase.rstrip())         # Retira os espaços da esquerda
print(frase.split())          # Divide a frase em que cada palavra é uma nova cadeia de caracter
print(frase.find('Android'))  # Vai procrar a palavra  na cadeia de caracteres e retornará -1 se não tiver


frase = 'Curso em Video Python'
dividido = frase.split()
print(dividido[0]) # Mostra 'Curso'
print(dividido[1]) # Mostra 'em'
print(dividido[2]) # Mostra 'Video'
print(dividido[3]) # Mostra 'Python'

# Começar o Desafio 22