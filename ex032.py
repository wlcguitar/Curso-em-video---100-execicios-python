"""Exercício Python 032: Faça um programa que leia um ano qualquer e mostre se ele é bissexto."""
from datetime import date

ano = int(input("Informe o ano ou 0 para analizar o ano atual: "))

if ano == 0:
    ano = date.today().year

if ano % 4 ==0:
    if ano % 100 == 0 and ano % 400 != 0:
        print("O ano de {} não e um ano bissexto.".format(ano))
    else:
        print("O ano de {} é um ano bissexto.".format(ano))
else:
    print("O ano de {} não e um ano bissexto.".format(ano))
