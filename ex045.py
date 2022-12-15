"""Exercício Python 045: Crie um programa que faça o computador jogar Jokenpô com você."""
from random import choice, random

print("[0]Pedra\n[1]Papel\n[2]Tesoura""")
i= int(input("Qual a sua opção: "))
lista = ["Pedra","Papel","Tesoura"]
player = lista[i]
cpu = choice(lista)


if player == cpu:
    print("Player jogou {}.".format(player))
    print("Computador jogou {}".format(cpu))
    print("Empate!!!")
elif player == "Pedra" and cpu == "Tesoura":  
    print("Player jogou {}.".format(player))
    print("Computador jogou {}.".format(cpu))
    print("Você venceu!!!")
elif player == "Pedra" and cpu == "Papel":
    print("Player jogou {}.".format(player))
    print("Computador jogou {}".format(cpu))
    print("Você perdeu!!!")
elif player == "Papel" and cpu == "Pedra":
    print("Player jogou {}.".format(player))
    print("Computador jogou {}.".format(cpu))
    print("Você venceu!!!")
elif player == "Papel" and cpu == "Tesoura":
    print("Player jogou {}.".format(player))
    print("Computador jogou {}".format(cpu))
    print("Você perdeu!!!")
elif player == "Tesoura" and cpu == "Papel":
    print("Player jogou {}.".format(player))
    print("Computador jogou {}.".format(cpu))
    print("Você venceu!!!")
elif player == "Tesoura" and cpu == "Pedra":
    print("Player jogou {}.".format(player))
    print("Computador jogou {}".format(cpu))
    print("Você perdeu!!!")
