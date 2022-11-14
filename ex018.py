'''Exercício Python 018: Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.'''
from math import radians, sin, cos, tan

ang = float(input("Qual o valor do ângulo: "))
radiano = radians(ang)
seno = sin(radiano)
cosseno = cos(radiano)
tangente = tan(radiano)

print("Seu seno e de {:.2f}.".format(seno))
print("Seu cosseno e de {:.2f}.".format(cosseno))
print("Sua tangente {:.2f}.".format(tangente))
