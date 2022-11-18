"""Exercício Python 035: Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo."""
s1 = float(input("Informe o 1º segmento: "))
s2 = float(input("Informe o 2º segmento: "))
s3 = float(input("Informe o 3º segmento: "))

if s1 > abs(s2 - s3) and s1 < abs(s2 + s3):
    print("segmentos podem formar um triângulo.")
else:
    print("Segmentos não podem formar um triângulo.")
