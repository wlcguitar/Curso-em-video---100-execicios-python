"""Exercício Python 041: A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
- Até 9 anos: MIRIM
- Até 14 anos: INFANTIL
- Até 19 anos: JÚNIOR
- Até 25 anos: SÊNIOR
- Acima de 25 anos: MASTER"""
from datetime import date

ano_atual = date.today().year
ano_nascimento = int(input("Qual ano de nascimento: "))
idade = ano_atual - ano_nascimento

if idade < 9:
    print("O atleta de {} anos, classificação MIRIM!!!".format(idade))
elif idade < 14:
    print("O atleta de {} anos, classificação INFANTIL!!!".format(idade))
elif idade < 19:
    print("O atleta de {} anos, classificação JÚNIOR!!!".format(idade))
elif idade < 25:
    print("O atleta de {} anos, classificação SÊNIOR!!!".format(idade))
else:
    print("O atleta de {} anos, classificação MASTER!!!".format(idade))
