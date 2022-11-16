"""Exercício Python 028: Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu."""
from random import randint
from time import sleep

print("=-"*20)
print("Sorteando número entre 0 e 5")
for i in range(5):
    sleep(0.5)
    print(".", end='', flush=True)
cpu = randint(0,5)

player = int(input("\nQual será o número sorteado: "))
print("Parábens você acertou!!!" if cpu == player else "Você errou o número certo e {}.".format(cpu))
print("=-"*20)
