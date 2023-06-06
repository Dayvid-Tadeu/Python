# Usando o exercicio anterior, leia os quatro alunos e mostre a ordem sorteada.
import random
a1 = input("Nome do Primeiro Aluno: ")
a2 = input("Nome do Segundo Aluno: ")
a3 = input("Nome do Terceiro Aluno: ")
a4 = input("Nome do Quarto Aluno: ")

lista = [a1, a2, a3, a4]
random.shuffle(lista)

print('A Ordem será: ')
print(lista)