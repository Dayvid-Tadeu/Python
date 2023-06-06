# Um professor quer sortear um dos quatro alunos para apagar o quadro.
# Faça um programa que leia e escreva o nome escolhido.
import random
a1 = input("Nome do Primeiro Aluno: ")
a2 = input("Nome do Segundo Aluno: ")
a3 = input("Nome do Terceiro Aluno: ")
a4 = input("Nome do Quarto Aluno: ")

lista = [a1, a2, a3, a4]
escolha = random.choice(lista)
print('O Aluno escolhido foi {}'.format(escolha))