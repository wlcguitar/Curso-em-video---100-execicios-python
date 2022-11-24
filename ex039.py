"""Exercício Python 039: Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento. Seu programa também deverá mostrar o tempo que falta ou que passou do prazo."""
from datetime import date

ano_atual = date.today().year
ano_nascimento = int(input("Qual ano de nascimento: "))
idade = ano_atual - ano_nascimento

if idade < 18:
    print("Você tem {} anos, ainda falta {} anos para se alistar.".format(idade, 18-idade))
elif idade == 18:
    print("Você tem {} anos, deve se alistar imediatamente.".format(idade))
else:
    print("Você tem {} anos, já deveria ter se alistado a {} anos.".format(idade, idade-18))
