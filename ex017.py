"""Exercício Python 017: Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo. Calcule e mostre o comprimento da hipotenusa."""
from math import sqrt

cateto_oposto = float(input("Valor do cateto oposto: "))
cateto_adjacente = float(input("Valor o cateto ajacente: "))
hipotenusa = sqrt(cateto_oposto ** 2 + cateto_adjacente ** 2 )

print("O valor da hipotenusa e de {:.2f}.".format(hipotenusa))
