"""Exercício Python 019: Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo na tela o nome do escolhido."""
from random import randint,choice

nomes = list()

for i in range(4):
    nomes.append(input("{}º aluno: ".format(i+1)))

sorteado = choice(nomes)
print("O aluno sorteado foi {}.".format(sorteado))
