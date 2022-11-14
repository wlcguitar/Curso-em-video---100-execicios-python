"""Exercício Python 020: O mesmo professor do desafio 019 quer sortear a ordem de apresentação de trabalhos dos alunos. Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada"""
from random import shuffle

nomes_alunos = list()

for i in range(4):
    nomes_alunos.append(input("{}º Aluno: ".format(i+1)))

shuffle(nomes_alunos)
print(nomes_alunos)
